from argparse import ArgumentParser

ip_table = [
58,    50,   42,    34,    26,   18,    10,    2,
60,    52,   44,    36,    28,   20,    12,    4,
62,    54,   46,    38,    30,   22,    14,    6,
64,    56,   48,    40,    32,   24,    16,    8,
57,    49,   41,    33,    25,   17,     9,    1,
59,    51,   43,    35,    27,   19,    11,    3,
61,    53,   45,    37,    29,   21,    13,    5,
63,    55,   47,    39,    31,   23,    15,    7]


file_help = ("File containing x")
parser = ArgumentParser('Apply IP initial permutation')
parser.add_argument('filename', help=file_help)
args = parser.parse_args()

#open file, read ciphertext
x_file = open(args.filename, 'r')
x = x_file.read().rstrip()

result = ""
for i in range(0, len(ip_table)):
    result += x[ip_table[i]-1]

print result
print "L0: {}".format(result[:32])
print "R0: {}".format(result[32:])