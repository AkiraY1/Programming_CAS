class character():
    def __init__(self, height, ability, eyeColor, hairColor, gender):
        self.height = height
        self.ability = ability
        self.eyeColor = eyeColor
        self.hairColor = hairColor
        self.gender = gender
    def changeAbility(self, newAbility):
        self.ability = newAbility

#Marvel characters
ironMan = character(185, "laser", "brown", "brown", "male")
captainAmerica = character(195, "strength", "blue", "brown", "male")
blackWidow = character(165, "russian spy", "brown", "red hair", "female")

print(ironMan.hairColor)

blackWidow.changeAbility("chinese spy")
print(blackWidow.ability)