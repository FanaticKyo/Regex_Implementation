"""
F19 11-411 NLP Assignment 1 Part 2
Substitution Cipher Encode/Decode Script
Ze Xuan Ong - 25 Jul 19

Encodes/decodes a given text file given a substitution cipher

USAGE: python decode.py MODE INPUT_FILE KEY_FILE
MODE - [encode/decode]; Default: decode
INPUT_FILE - .txt file containing text to encode/decode
KEY_FILE - .txt file containing a key

No error checking/uniqueness checking is performed on input key file.
Assumes user has checked validity of mapping. Assumes that the
key file contains 52 lines of the form 'A B', where the first
character maps to the second character in an encoding scheme.

"""


import sys


def read_key_file(filename, encoding=True):
    """
    Convert a cipher key file into a Python dictionary
    :param filename: filename of key file
    :param encoding: boolean indicating the encoding/decoding mode, True indicates encoding mode
    :return: dictionary containing the substitution cipher
    """

    d = {}
    with open(filename, "r") as f:
        for line in f:
            tokens = line.split()
            if len(tokens) != 2:
                continue
            if encoding:
                d[ord(tokens[0])] = ord(tokens[1])
            else:
                d[ord(tokens[1])] = ord(tokens[0])
    return d


def read_input_file(filename):
    """
    Read input from input file into string
    :param filename: filename of input file
    :return: string containing all contents of input file
    """

    with open(filename, "r") as f:
        return f.read()

# Main program
if __name__ == "__main__":

    # Ensure exactly two arguments
    if len(sys.argv) != 4:
        print("Usage: python decode.py MODE INPUT_FILE KEY_FILE")
        sys.exit(1)

    ENCODE_MODE = True if sys.argv[1] == 'encode' else False
    INPUT_FILE = sys.argv[2]
    KEY_FILE = sys.argv[3]

    # Check input file type
    if not (INPUT_FILE.endswith(".txt") and KEY_FILE.endswith(".txt")):
        print("Error: INPUT_FILE and KEY_FILE must be .txt files")
        sys.exit(1)

    # Get cipher dictionary
    key = read_key_file(KEY_FILE, encoding=ENCODE_MODE)

    # Read input
    input_text = read_input_file(INPUT_FILE)

    # Translate file
    # NOTE: translate takes a dictionary with ascii number key value pairs
    output_text = input_text.translate(key)

    # Print
    print(output_text)



