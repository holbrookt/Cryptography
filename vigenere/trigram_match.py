from argparse import ArgumentParser
from fractions import gcd

limit_help = "Only produce trigrams up to a specified index."
file_help = ("File containing ciphertext (text should be all capitals, "
             "no spaces, no newlines.")
parser = ArgumentParser('Find max coincidences in overlapped text')
parser.add_argument('filename', help=file_help)
parser.add_argument('-l', '--limit', type=int, default=0, help=limit_help)
args = parser.parse_args()

#open file, read ciphertext
ctext_file = open(args.filename, 'r')
ctext = ctext_file.read().rstrip()

trigram_positions = {}

# limit the trigram search to a max string index if specified
limit = args.limit if args.limit > 0 else len(ctext)
limit = len(ctext) if limit > len(ctext) else limit

for i in range(0, limit - 2):
    #try every trigram, but only once
    trigram = ctext[i:i+3]
    if trigram in trigram_positions.keys():
        continue
    matches = []
    for location in range(0, len(ctext) - 2):
        #iterate over the length of the string and keep track of matches
        if trigram == ctext[location:location+3]:
            matches.append(location)
    trigram_positions[trigram] = matches

trigram_differences = {}
for trigram, locations in trigram_positions.items():
    # loop only for every trigram found in multiple locations
    if len(locations) < 2:
        continue
    print "\'{}\' locations: {}".format(trigram, locations)
    
    # find differences between all locations and first location
    differences = []
    for l in locations[1:]:
        differences.append(l - locations[0])
    trigram_differences[trigram] = differences

# calculate and list GCDs of interest for the differences for every trigram
for trigram, differences in trigram_differences.items():
    for diff in differences:
        diff_gcds = [gcd(diff, test_diff) for test_diff in differences]
    print "\'{}\' GCDs of location differences: {}".format(trigram, diff_gcds)