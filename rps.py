import random, time

players = []

def play(index):
    global players

    while True:
        print("------------ Welcome to Rock Paper Scissors! -------------")
        user_action = input("Choose one of the following: Rock [r], Paper [p] or Scissors [s]: ").lower()
        computer_action = random.choice(["r", "p", "s"])
        if user_action == computer_action:
            print(f"Both players selected {user_action}. It's a tie!")
        else:
            if user_action == "r":
                if computer_action == "s":
                    print("Rock smashes scissors! You win!")
                    players[index][1] += 1
                if computer_action == "p":
                    print("Paper covers rock! You lose.")
            if user_action == "p":
                if computer_action == "r":
                    print("Paper covers rock! You win!")
                    players[index][1] += 1
                if computer_action == "s":
                    print("Scissors cuts paper! You lose.")
            elif user_action == "s":
                if computer_action == "p":
                    print("Scissors cuts paper! You win!")
                    players[index][1] += 1
                if computer_action == "r":
                    print("Rock smashes scissors! You lose.")
        time.sleep(1)
        print(f"Your score is: {players[index][1]}")
        time.sleep(1)
        playAgain = input("Would you like to play again? [y/n]: ")
        if playAgain == "y":
            continue
        if playAgain == "n":
            main()
        

def main():
    global players
    registered = False
    print("---------------------------------------------------")
    print("Remember, to quit this program press ctrl-z or ctrl-c")
    name = input("Enter username: ")

    for p in players:
        if name in p:
            registered = True
            index = players.index(p)
            print(f"Current Score: {p[1]}")
    
    if registered == True:
        play(index)
    if registered == False:
        players.append([name, 0])
        index = len(players)-1
        play(index)

while True:
    main()