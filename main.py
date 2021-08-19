import os
import re


def main():
    directory = input("Directory: ")
    file_name = input("Filename: ")
    key = file_name.replace("-", "_")
    out = open(os.path.join("output", file_name + ".json"), "w")
    out.write("{\n")
    out.write(f"  \"Key\": \"{key}\",\n")
    author = input("Author: ")
    out.write(f"  \"Author\": \"{author}\"")
    beat_nr = 0
    for filename in sorted(os.listdir(os.path.join("input", directory)), key=lambda fname: get_note_nr(fname)):
        f = os.path.join("input", directory, filename)
        if not os.path.isfile(f):
            raise Exception("Please make sure there are only .mcfunction files in the notes directory.")
        file = open(f, "r")
        nr = get_note_nr(filename)
        wait = nr - beat_nr
        beat_nr = nr
        if beat_nr != 0:
            out.write(f",\n  \"Wait\": {wait}")
        for x in file:

            if x.startswith("playsound "):
                instrument = re.search("note_block\\.(.*) record", x).group(1)
                volume = float(re.search("\\^ ([01]\\.?\d?\d? )", x).group(1))
                pitch = re.search("([012]\\.\d{6})", x).group(1)
                if instrument is None or volume is None or pitch is None:
                    print(x)
                    raise Exception("Malformatted note")
                out.write(
                  f",\n  \"PlaySound\": [\"block_note_block_{instrument}\", {pitch}, {volume:.2f}]"
                )
    out.write("\n}")
    print("File created at "+ os.path.join("output", file_name + ".json"))


def get_note_nr(filename: str):
    return int(filename.replace(".mcfunction", ""))


if __name__ == '__main__':
    main()
