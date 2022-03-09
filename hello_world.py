print("Hello! My name is Bob! I am here to be your friend :)")
print("What is your name?")
name = input()

print(f"Nice to meet you {name}")
print("Do you enjoy class?")
answer = input().lower()
if answer == "yes":
    print("Great! I love school too!")
if answer == "no":
    print("Oh that's too bad, I think Akira's great :(")
else:
    print("I didn't catch that, I'm sorry...")