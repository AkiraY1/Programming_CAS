message = input()
key = 4

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
newMessage = ''

for l in message:
    position = ALPHABET.find(l)
    newPosition = position + key
    newLetter = ALPHABET[newPosition]
    print(newLetter)