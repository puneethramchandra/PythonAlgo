class PlayerChar:  #naming Convention for class
    # Class object Attribute all objects can use this
    membership=True
    def __init__(self, name, age): #init is a magic method
        if (PlayerChar.membership):
            self.name = name
            self.age = age

    def shout(self):
       return print(f'My name is {self.name}')




player1 = PlayerChar('Puneeth',21)
player2 = PlayerChar("Rupa",46)



print(player1) #Different memory locations suggests different objects
print(player2)
print(player1.name)
print(player2.name)
print(player2.age)
print(player2.shout())