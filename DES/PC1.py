from argparse import ArgumentParser

indices = [
57,   49,    41,   33,    25,    17,    9,
 1,   58,    50,   42,    34,    26,   18,
10,    2,    59,   51,    43,    35,   27,
19,   11,     3,   60,    52,    44,   36,
63,   55,    47,   39,    31,    23,   15,
 7,   62,    54,   46,    38,    30,   22,
14,    6,    61,   53,    45,    37,   29,
21,   13,     5,   28,    20,    12,    4]


file_help = ("File containing key")
parser = ArgumentParser('Apply PC1')
parser.add_argument('filename', help=file_help)
args = parser.parse_args()

#open file, read ciphertext
key_file = open(args.filename, 'r')
key = key_file.read().rstrip()

k_plus = ""
for i in range(0, len(indices)):
    k_plus += key[indices[i]-1]

print k_plus
#print "".join(k_plus)