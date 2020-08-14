class PlayerChar:#naming Convention for class
    def __init__(self,name, age): #init is a magic method
        self.name= name
        self.age=age

    def run(self):
       print('run')
       return 'Done'



player1 = PlayerChar('Puneeth',21)
player2= PlayerChar("Rupa",46)

print(player1) #Different memory locations suggests different objects
print(player2)
print(player1.name)
print(player2.name)
print(player2.age)
print(player2.run())