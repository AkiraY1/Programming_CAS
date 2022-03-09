import random, time #Don't forget to import these!

# rps.py is a basic rock paper scissors program that allows multiple users to 
# play in the same session. I did not add in any code to catch 
# any input that is not expected. For example, if the user types in something 
# other than r, p or s when playing the game, it will not alert the user and
# just skip to asking if you would like to play again.

players = []

def play(index): #Accepts a variable index that will be used to update player scores
    global players #Allows the function to access the list players (otherwise the list would exist solely outside the function)

    while True: #All in a while loop so that you can play over and over again
        print("------------ Welcome to Rock Paper Scissors! -------------")
        user_action = input("Choose one of the following: Rock [r], Paper [p] or Scissors [s]: ").lower() #.lower() makes the input lowercase
        computer_action = random.choice(["r", "p", "s"])
        if user_action == computer_action:
            print(f"Both players selected {user_action}. It's a tie!")
        else:
            if user_action == "r":
                if computer_action == "s":
                    print("Rock smashes scissors! You win!")
                    players[index][1] += 1 #Uses the variable index to increase the current player's score by 1 (var += 1 means "increase var by 1")
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
        time.sleep(1) #Waits for 1 second
        print(f"Your score is: {players[index][1]}") #Prints the player's score
        time.sleep(1)
        playAgain = input("Would you like to play again? [y/n]: ")
        if playAgain == "y":
            continue #Goes back to the top of the while loop and starts over again
        if playAgain == "n":
            main() #Calls the main function
        

def main():
    global players
    registered = False #registered is used to check if a player is registered or not
    print("---------------------------------------------------")
    print("Remember, to quit this program press ctrl-z or ctrl-c")
    name = input("Enter username: ")

    for p in players: #This is what we did last class, iterating through the over players list to check if each individual list has the username the person just typed in
        if name in p: #Checks if the user is in one of the lists inside the players list
            registered = True
            index = players.index(p) #Retrieves the index of the list inside the players list
            print(f"Current Score: {p[1]}")
    
    # Notice there is no "if name not in p", that's because registered is initially set to False (the computer assumes 
    # the user is not registered, so we only need to check if they ARE registered)

    if registered == True:
        play(index) #If they are registered, calls the play function from above
    if registered == False:
        players.append([name, 0]) #Like we did last class, adds a player to the players list
        #len() is a method that retrieves the length of an iterable (in this case the players list), and then 
        #substracts 1 because we start counting at 0, not 1, for indices
        index = len(players)-1 
        play(index)
        # Notice that when it calls the play() function, it passes along the variable index, which contains the 
        # position of the current player in the players list (which is necessary to update players' scores)

# While loop means that the program will never end by itself, so you can keep playing as long as your heart desires :)
while True:
    main()