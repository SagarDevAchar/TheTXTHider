import cv2
import numpy as np

from datetime import datetime as dt
from os import system, listdir
import msvcrt
from tqdm import trange


def get_stegano_or(char_bin: str, size: tuple, depth: int):
    or_arr = np.zeros(size, dtype=np.uint8)

    c = 0
    for x in trange(0, len(char_bin), depth, ncols=100, unit=' bytes', desc='Encoding'):
        k = c % size[2]
        j = (c // size[2]) % size[1]
        i = c // (size[2] * size[1])

        try:
            or_arr[i, j, k] |= int(char_bin[x: x+depth], 2)
        except IndexError:
            break

        c += 1

    return or_arr


SECTION_SEPERATOR = '\n' + '-' * 125 + '\n'

LOGO = """
            ████████╗██╗  ██╗███████╗    ████████╗██╗  ██╗████████╗    ██╗  ██╗██╗██████╗ ███████╗██████╗ 
            ╚══██╔══╝██║  ██║██╔════╝    ╚══██╔══╝╚██╗██╔╝╚══██╔══╝    ██║  ██║██║██╔══██╗██╔════╝██╔══██╗
               ██║   ███████║█████╗         ██║    ╚███╔╝    ██║       ███████║██║██║  ██║█████╗  ██████╔╝
               ██║   ██╔══██║██╔══╝         ██║    ██╔██╗    ██║       ██╔══██║██║██║  ██║██╔══╝  ██╔══██╗
               ██║   ██║  ██║███████╗       ██║   ██╔╝ ██╗   ██║       ██║  ██║██║██████╔╝███████╗██║  ██║
               ╚═╝   ╚═╝  ╚═╝╚══════╝       ╚═╝   ╚═╝  ╚═╝   ╚═╝       ╚═╝  ╚═╝╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝
               
                            █▀▄ █ █   █▀▀ █▀█ █▀▀ █▀█ █▀▄   █▀▄ █▀▀ █ █   █▀█ █▀▀ █ █ █▀█ █▀▄
                            █▀▄  █    ▀▀█ █▀█ █ █ █▀█ █▀▄   █ █ █▀▀ ▀▄▀   █▀█ █   █▀█ █▀█ █▀▄
                            ▀▀   ▀    ▀▀▀ ▀ ▀ ▀▀▀ ▀ ▀ ▀ ▀   ▀▀  ▀▀▀  ▀    ▀ ▀ ▀▀▀ ▀ ▀ ▀ ▀ ▀ ▀
""" + SECTION_SEPERATOR

while True:
    print(LOGO)

    print("Press H to Hide Text in an Image")
    print("Press R to Retrieve Text from an Image")

    print("\n\rWaiting for your Input...", end="")
    MODE_INPUT = msvcrt.getch()

    if MODE_INPUT == b'h' or MODE_INPUT == b'H':
        print("\rHiding Mode ACTIVATED!\t\t\t")
        print(SECTION_SEPERATOR)

        try:
            files = listdir('FILES')
            assert 'text.txt' in files and ('image.jpg' in files or 'image.jpeg' in files or 'image.png' in files)

            IMG_FORMAT = ""
            for filename in files:
                filename = filename.split('.')
                if filename[1] == 'jpg' or filename[1] == 'jpeg' or filename[1] == 'png':
                    IMG_FORMAT = filename[1]
                    break

            BLANK_IMAGE = cv2.imread(rf"FILES\image.{IMG_FORMAT}", cv2.IMREAD_COLOR)
            H, W, D = BLANK_IMAGE.shape
            BIT_COUNT = W * H * D * 2
            BYTE_COUNT = BIT_COUNT // 8

            print(f"Resolution of 'image.{IMG_FORMAT}' = {W} x {H}")
            print(f"No. of bits of plaintext that can be hidden in this image = {BIT_COUNT}")

            print(f"\nIn simple terms, {BYTE_COUNT} characters can be stored in this image")

            HIDING_TEXT = open(r'FILES\text.txt', 'r').read()
            TXT_SIZE = len(HIDING_TEXT)
            HIDING_CHARS = list(map(ord, list(HIDING_TEXT)))
            HIDING_BIN = "".join([f"{x:08b}" for x in HIDING_CHARS])

            print(f"\nThe TXT file has {TXT_SIZE} characters which ",
                  end=f"is in the {BYTE_COUNT} character limit\nThe text consumes {TXT_SIZE * 100 / BYTE_COUNT :.3f} % of the available space\n\n" if TXT_SIZE <= BYTE_COUNT else f"EXCEEDS THE {BYTE_COUNT} CHARACTER LIMIT\nOnly {BYTE_COUNT * 100 / TXT_SIZE :.3f} % of the text can be encoded...\n\n")

            STEGANO_ERASED_IMAGE = BLANK_IMAGE & 0b11111100
            STEGANO_OR = get_stegano_or(HIDING_BIN, (H, W, 3), 2)
            STEGANO_WRITTEN_IMAGE = STEGANO_ERASED_IMAGE | STEGANO_OR

            cv2.imwrite(rf"FILES\image_stegano.png", STEGANO_WRITTEN_IMAGE)

            print(f"\nGenerated 'image_stegano.png'!\nYou can find it in the 'FILES' folder")

        except FileNotFoundError:
            print("Looks like you have lost the 'FILES' folder!\nUnfortunately, I cannot work without that...")
        except AssertionError:
            print("I don't seem to find all the files necessary for me to work...")
            print("How about you ensure that you have a 'text.txt' and 'image.jpg/jpeg/png' in the 'FILES' folder and try again?")

    elif MODE_INPUT == b'r' or MODE_INPUT == b'R':
        print("\rRetrieval Mode ACTIVATED!\t\t\t")
        print(SECTION_SEPERATOR)

        try:
            files = listdir('FILES')
            assert 'image_stegano.png' in files

            STEGANO_IMAGE = cv2.imread(r'FILES\image_stegano.png', cv2.IMREAD_COLOR)
            H, W, D = STEGANO_IMAGE.shape

            STEGANO_DATA = "".join([f"{x:02b}" for x in (STEGANO_IMAGE & (0xFF >> 6)).reshape((1, W * H * D))[0]])
            STEGANO_DATA = STEGANO_DATA[:STEGANO_DATA.index('00000000')+1]
            print("\nRecovering %d bits of data from 'image_stegano.png'\n" % len(STEGANO_DATA))

            print("RECOVERED DATA:\n")
            for i in range(0, len(STEGANO_DATA), 8):
                print(chr(int(STEGANO_DATA[i: i + 8], 2)), end='')
            print('\n')
        except FileNotFoundError:
            print("Looks like you have lost the 'FILES' folder!\nUnfortunately, I cannot work without that...")
        except AssertionError:
            print("I don't seem to find the file necessary for me to work...")
            print("How about you ensure that you have a 'image_stegano.png' in the 'FILES' folder and try again?")
    else:
        print("\rWell, that was unexpected!")

    print(SECTION_SEPERATOR)
    input("Press ENTER to start over")
    system('cls')
