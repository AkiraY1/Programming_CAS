word = input()
opposite = []

for w in word:
    opposite.insert(0, w)

if opposite == list(word):
    print("Is a palindrome")