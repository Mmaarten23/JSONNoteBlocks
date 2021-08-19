## Noteblock Studio to PokeFind scripting
This project takes the output from [Open note block studio](https://opennbs.org/) and converts it into a script acceptable by the [Lucille games](https://www.lucillegames.com/) scripting system.

### Requirements
- Open Note Block studio [(3.8.3+)](https://opennbs.org/)
- Python [(3.8+)](https://www.python.org/downloads/)

### How to
1. Clone this repository locally
2. In Open NBS, import the song in midi format/create your own song
3. Export the Open NBS project as data pack<sup>1</sup>
4. Unzip the result and navigate to the ``data/<datapackname>/functions`` directory
5. Copy the ``notes`` folder and paste it in the input folder of this project<sup>2</sup>
6. Open a command line in this project
7. Run ``py main.py``
8. When asked for a directory, enter the name you gave to the ``notes`` folder
9. When asked for a filename, enter the name you wish to use for the output file (without extension)<sup>3</sup>
10. Fill in your Author signature when asked
11. The script will be generated in the output directory


<sup>1</sup> Make sure that in the top right of the Open NBS window, it says "Data pack only" or "Fully compatible". If it says "Resource pack only", you will have to transpose the notes.

<sup>2</sup> It is advised to rename the ``notes`` folder to a more descriptive name

<sup>3</sup> The filename will also be used as the script key with dashes replaced by underscores


### Example
The megalovania example was created using the following arguments:
````
Directory: megalovania
Filename: megalovania
Author: Mmaarten
````

### Support
Contact @Mmaarten#1769 on discord for help!
