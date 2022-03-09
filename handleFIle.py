
def chatbot():
    name = input()
    print(f"Hello {name}")
    print("Do you like cookies?")
    choice = input()
    if choice == "yes":
        print("Great, I love cookies too!")
    else:
        print("The cookie monster disapproves")

while True:
    chatbot()