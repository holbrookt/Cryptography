from argparse import ArgumentParser

pc2_table = [
14,    17,   11,    24,     1,    5,
 3,    28,   15,     6,    21,   10,
23,    19,   12,     4,    26,    8,
16,     7,   27,    20,    13,    2,
41,    52,   31,    37,    47,   55,
30,    40,   51,    45,    33,   48,
44,    49,   39,    56,    34,   53,
46,    42,   50,    36,    29,   32]


file_help = ("File containing key")
parser = ArgumentParser('Apply PC2')
parser.add_argument('filename', help=file_help)
args = parser.parse_args()

#open file, read ciphertext
key_file = open(args.filename, 'r')
key = key_file.read().rstrip()

result = ""
for i in range(0, len(pc2_table)):
    result += key[pc2_table[i]-1]

print result