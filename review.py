class character():
    def __init__(self, hairColor, superpower):
        self.hairColor = hairColor
        self.superpower = superpower
        self.
    
    def changeHairColor(self, newHairColor):
        self.hairColor = newHairColor

ironMan = character("black")
print(ironMan.hairColor)
ironMan.changeHairColor("brown")
print(ironMan.hairColor)