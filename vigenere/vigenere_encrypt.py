from argparse import ArgumentParser

parser = ArgumentParser('Encrypt using vignere cypher')
parser.add_argument('keyword')
parser.add_argument('plaintext')
args = parser.parse_args()

plaintext = [char for char in args.plaintext if char != ' ']
plaintext_string = ""
for char in plaintext:
    plaintext_string += char
print plaintext_string

key = [ord(char) - 97 for char in args.keyword]
plaintext_nums = [ord(char) - 97 for char in plaintext]
ciphertext = ""
iKey = 0 
for num in plaintext_nums:
    iKey = iKey % len(key)
    ciphertext += chr(((num + key[iKey]) % 26) + 97)
    iKey += 1

print ciphertext
