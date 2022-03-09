players = []
name = input()
name2 = input()

players.append([name, 0])
players.append([name2, 0])

print(players)

for i in players:
    if name in i:
        print("The player has already registered!")
        #Printing out the score for bob
        print(i[1])
        i[1] = i[1] + 1

for person in players:
    if person[0] == "joe":
        person[1] = person[1] + 1

print(players)