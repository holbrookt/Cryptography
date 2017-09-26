from argparse import ArgumentParser

limit_help = "Only produce trigrams up to a specified index."
file_help = ("File containing ciphertext (text should be all capitals, "
             "no spaces, no newlines.")
parser = ArgumentParser('Find max coincidences in overlapped text')
parser.add_argument('filename', help=file_help)
parser.add_argument('-v', '--verbose', action='store_true', default=False)
parser.add_argument('-l', '--limit', type=int, default=0, help=limit_help)
args = parser.parse_args()

#open file, read ciphertext
ctext_file = open(args.filename, 'r')
ctext = ctext_file.read().rstrip()

coincidence_dict = {}
max_coincidences = 0
max_offset = 0

# limit the offset to a value if specified
limit = args.limit if args.limit > 0 else len(ctext)
limit = len(ctext) if limit > len(ctext) else limit

for offset in range(1, limit):
    #try every offset
    num_coincidences = 0
    for i in range(0, len(ctext) - offset):
        #iterate over the length of the string and check equality
        if ctext[i] == ctext[i+offset]:
            num_coincidences += 1
    coincidence_dict[offset] = num_coincidences
    if num_coincidences > max_coincidences:
        max_coincidences = num_coincidences
        max_offset = offset
    if args.verbose:
        print "Offset:       {}".format(offset)
        print "Coincidences: {}".format(num_coincidences)

print "Offset with most coincidences: {}".format(max_offset)
print "       number of coincidences: {}".format(max_coincidences)
