[![Active Version](https://img.shields.io/badge/version-v2022.07.19-blue)](https://github.com/SagarDevAchar/TheTXTHider/releases/download/release/The.TXT.Hider.v2022.07.19.zip)
[![GitHub issues](https://img.shields.io/github/issues/SagarDevAchar/TheTXTHider)](https://github.com/SagarDevAchar/TheTXTHider/issues)
[![GitHub license](https://img.shields.io/github/license/SagarDevAchar/TheTXTHider)](https://github.com/SagarDevAchar/TheTXTHider/blob/main/LICENSE)
[![SHA256 Checksum](https://img.shields.io/badge/sha256-81abab7934b36d9ccf490b0c57b60b6cf2773844a439434346bd60da45fc7798-red)](https://emn178.github.io/online-tools/sha256_checksum.html)

![TPM TMP Logo 1](https://user-images.githubusercontent.com/51400137/183991932-b38b05ec-81bf-454f-bb84-9358d8bacd83.png)

# [The TXT Hider](https://github.com/SagarDevAchar/TheTXTHider/releases/download/release/The.TXT.Hider.v2022.07.19.zip)

Part 1 of the **Steganography Made Fun!** Toolkit. Click on the heading above to download the latest release

## About the Project

![TPM TMP Card StegDef](https://user-images.githubusercontent.com/51400137/183993442-544ff0b9-dea6-45d6-bd98-073dddf2c3fd.png)

Steganography, although seems complicated is a very interesting process. It may involve studying the properties of the original message for better concealing of data. Encryption may also be employed before Steganography or Steganography may be applied to an encrypted message to make the data imperceptible

Image Steganography usually stores data in the LSB bits of the pixel brightness levels. 1-4 bits are used commonly where more the number of bits induces more noise into the encoded message. The amount of data that can be stored in a image is proportional to the resolution of the image.

**Steganography Made Fun!** is an Image Steganography Toolkit which makes Steganography enjoyable. The toolkit has three parts divided into three repositories:
- Part 1: [The TXT Hider](https://sagardevachar.github.io/TheTXTHider/) (This Repository)
- Part 2: [The MP3 Photographer](https://sagardevachar.github.io/TheMP3Photographer/)
- Part 3: [The PNG Musician](https://sagardevachar.github.io/ThePNGMusician/)

## Release Directory Structure

- `FILES\` : This is where the program looks for files and writes new files into
- `LICENSE` : GNU GPL v3.0 License for [The TXT Hider](https://github.com/SagarDevAchar/TheTXTHider)
- `README.txt` : Release Information
- `The TXT Hider.exe` : Executable for Windows Devices (built using PyInstaller)

## Repository Structure

- `FILES\` : This is where the program looks for files and writes new files into
- `LICENSE` : GNU GPL v3.0 License for [The TXT Hider](https://github.com/SagarDevAchar/TheTXTHider)
- `README.md` : Repository Information
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

## Disclaimer

- I do not own any rights to the images or music in this repository. All rights are reserved by the respective artists and record labels
- Most Antivirus Softwares falsely tag the EXE as suspicious piece of software. Please whitelist the EXE on your device to use it
- The provided SHA256 Checksum is for the EXE provided and can be verified if required

## Acknowledgements and References

- ASCII Art by: [TextKool](https://textkool.com/en)
- Quickstart: [Secrets Hidden in Images (Steganography) - Computerphile](https://youtu.be/TWEXCYQKyDc)

![TPM TMP Logo 0](https://user-images.githubusercontent.com/51400137/183991799-2e104795-d1ba-452c-9284-9b44e0ffb9e6.png)

![TPM TMP Card TXT](https://user-images.githubusercontent.com/51400137/183991820-0c4a8a7a-c072-4bb8-8d8e-25838dc6dbfb.png)

