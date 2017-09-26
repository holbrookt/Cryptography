from argparse import ArgumentParser
from fractions import gcd
import string
import sys

english_freqs = {'A': 0.082, 'N': 0.067,
                 'B': 0.015, 'O': 0.075,
                 'C': 0.028, 'P': 0.019,
                 'D': 0.043, 'Q': 0.001,
                 'E': 0.127, 'R': 0.060,
                 'F': 0.022, 'S': 0.063,
                 'G': 0.020, 'T': 0.091,
                 'H': 0.061, 'U': 0.028,
                 'I': 0.070, 'V': 0.010,
                 'J': 0.002, 'W': 0.023,
                 'K': 0.008, 'X': 0.001,
                 'L': 0.040, 'Y': 0.020,
                 'M': 0.024, 'Z': 0.001}
english_Ic = 0.065


def find_letter_freq(str, char):
    freq = 0
    for i in str:
        if char == i:
            freq += 1
    return freq

def subtract_strings_mod26(str1, str2):
    if (len(str1) != len(str2)):
        raise Exception("Strings should be same length!")

    r_str = ""
    nums1 = [ord(char) - ord('A') for char in str1]
    nums2 = [ord(char) - ord('A') for char in str2]
    for i in range(0, len(nums1)):
        r_str += chr(((nums1[i] - nums2[i]) % 26) + ord('A'))
    return r_str


file_help = ("File containing ciphertext (text should be all capitals, "
             "no spaces, no newlines.")
parser = ArgumentParser('Decrypt vigenere-encypted ciphertext '
                        'with known keylength.')
parser.add_argument('filename', help=file_help)
parser.add_argument('keylength', type=int)
args = parser.parse_args()

keylength = args.keylength
if keylength < 1:
    print "Please specifiy a keylength greater than 0.\n"
    sys.exit(1)

#open file, read ciphertext
ctext_file = open(args.filename, 'r')
ctext = ctext_file.read().rstrip()

# create substrings based on keylength
substrings = {}
for i in range(1, keylength+1):
    substrings[i] = ctext[i-1::keylength]

key = {}
substring_Mg_values = {}
for ki, substring in substrings.items():
    for g in range(0, 26):
        temp_sum = 0
        for i in range(0, 26):
            # for 0 to 25
            letter = chr(((i + g) % 26) + ord('A'))
            pi = english_freqs[chr(i + ord('A'))]
            temp_sum += pi * find_letter_freq(substring, letter)
        substring_Mg_values[g] = temp_sum / len(substring)

    min_diff = 99999999
    for g, value in substring_Mg_values.items():
        if abs(value - english_Ic) < min_diff:
            key[ki] = g
            min_diff = abs(value - english_Ic)

print "Key values: {}".format(key)
keyword = "".join([string.ascii_uppercase[x] for x in key.values()])
print "Keyword:    {}".format(keyword)

decrypt_string = keyword * ((len(ctext) / keylength) + 1)
decrypt_string = decrypt_string[:len(ctext)]

print "Decrypted message:"
print"{}".format(subtract_strings_mod26(ctext, decrypt_string))