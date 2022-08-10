![image](https://user-images.githubusercontent.com/51400137/183978234-0502b007-17e7-4ad8-8023-0ce10b1a2a56.png)

[![Active Version](https://img.shields.io/badge/version-v2022.07.19-blue)](https://github.com/SagarDevAchar/TheTXTHider/releases/download/release/The.TXT.Hider.v2022.07.19.zip)
[![GitHub issues](https://img.shields.io/github/issues/SagarDevAchar/TheTXTHider)](https://github.com/SagarDevAchar/TheTXTHider/issues)
[![GitHub license](https://img.shields.io/github/license/SagarDevAchar/TheTXTHider)](https://github.com/SagarDevAchar/TheTXTHider/blob/main/LICENSE)

# The TXT Hider

An LSB2 Steganography Encoder / Decoder which hides plain text in PNG Images

## About the Project

This is first part of the **Steganography Made Fun!** toolkit

The toolkit has three parts divided into three repositories:

- Part 1: [The TXT Hider](https://sagardevachar.github.io/TheTXTHider/) (This Repository)
- Part 2: [The MP3 Photographer](https://sagardevachar.github.io/TheMP3Photographer/)
- Part 3: [The PNG Musician](https://sagardevachar.github.io/ThePNGMusician/)

## Repository Structure

- `FILES\` : This is where the program looks for files and writes new files into
- `LICENSE` : GNU GPL v3.0 License for [The TXT Hider](https://github.com/SagarDevAchar/TheTXTHider)
- `README.md` : Here you are!
- `install_requirements.bat` : Installs the necessary package requirements using `pip` (Requires `pip` access in `PATH`)
- `The TXT Hider.py` : Source Code

## Usage Instructions

1. Just let things be where they are (relatively)
2. For Steganography:
    - Place your target image in **PNG** or **JPG** or **JPEG** format with the file name `image` under the `FILES\` directory
    - Type in your text in the `text.txt` file under the `FILES\` directory
    - Run `The TXT Hider.py` using the IDE of your choice or via CMD using the `python "The TXT Hider.py"` command
    - Obtain the Steganographically Encoded PNG file in the `FILES\` directory with the name `image_stegano.png`
3. For Reverse Steganography
    - Place the encoded image with name `image_stegano.png` under the `FILES\` directory
    - Run `The TXT Hider.py` using the IDE of your choice or via CMD using the `python "The TXT Hider.py"` command
    - Observe the decoded text on the command line interface


## Requirements

- **Operating System:** Windows
- **Python Version:** 3.5+
- **Packages:** [TQDM](https://tqdm.github.io/), [NumPy](https://numpy.org/), [OpenCV](https://opencv.org/)

You can install the required packages manually or by running the `install_requirements.bat`. You can always create a virtual environment to prevent your version critical installations from being modified (You need to switch to the virtual environment before running the batch file)

## Disclaimer

I do not own any rights to the images or music in this repository. All rights are reserved by the respective artists and record labels

## Acknowledgements and References

- ASCII Art by: [TextKool](https://textkool.com/en)
- Quickstart: [Secrets Hidden in Images (Steganography) - Computerphile](https://youtu.be/TWEXCYQKyDc)

