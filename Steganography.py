import sys
import argparse

from libs import audio_steganography
from libs import image_steganography
from libs import text_steganography
from libs import video_steganography

use_text_encode = "python3 ./Steganography.py -t -e <location of file>"
use_text_decode = "python3 ./Steganography.py -t -d <location of file>"

use_audio_encode = "python3 ./Steganography.py -a -e <location of file>"
use_audio_decode = "python3 ./Steganography.py -a -d <location of file>"

use_video_encode = "python3 ./Steganography.py -v -e <location of file>"
use_video_decode = "python3 ./Steganography.py -v -d <location of file>"

use_image_encode = "python3 ./Steganography.py -i -e <location of file>"
use_image_decode = "python3 ./Steganography.py -i -d <location of file>"

use_help = "python3 ./Steganography.py -h -----> help"


def symbols():
    print("_" * 60)
    print("_" * 60)
    print("      ")
    print("_" * 60)
    print("      ")
    print("                                                     STEGANOGRAPHY")
    print("      ")
    print("_" * 60)
    print("      ")
    print("_" * 60)
    print("      ")
    print("                                     M A D E  B Y  K A U S I K  A N D  R O N I T ")
    print("      ")
    print("_" * 60)
    print("_" * 60)
    print("PROJECT STARTED")
    print("      ")
    print("_" * 60)
    print("=" * 60)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--audio', action='store_true', help="For audio file")
    parser.add_argument('-t', '--text', action='store_true', help="For text file")
    parser.add_argument('-v', '--video', action='store_true', help="For video file")
    parser.add_argument('-i', '--image', action='store_true', help="For image file")
    parser.add_argument('-e', '--encode', action='store_true', help="For encoding")
    parser.add_argument('-d', '--decode', action='store_true', help="For decoding")
    parser.add_argument('filename')
    args = parser.parse_args()
    c = 0
    t = True
    if args.filename:
        symbols()
        if args.audio and args.encode and t:
            audio_steganography.Audio_steganography(args.filename, 0)
            t = False
        elif args.audio and args.decode and t:
            audio_steganography.Audio_steganography(args.filename, 1)
            t = False
        elif args.text and args.encode and t:
            text_steganography.Text_steganography(args.filename, 0)
            t = False
        elif args.text and args.decode and t:
            text_steganography.Text_steganography(args.filename, 1)
            t = False
        elif args.video and args.encode and t:
            video_steganography.Video_Steganography(args.filename, 0)
            t = False
        elif args.video and args.decode and t:
            video_steganography.Video_Steganography(args.filename, 1)
            t = False
        elif args.image and args.encode and t:
            image_steganography.Image_steganography(args.filename, 0)
            t = False
        elif args.image and args.decode and t:
            image_steganography.Image_steganography(args.filename, 1)
            t = False
        else:
            c = 1
    else:
        symbols()
        parser.print_help()
        sys.exit(0)
    if c == 1:
        symbols()
        parser.print_help()
        sys.exit()


if __name__ == "__main__":
    main()
