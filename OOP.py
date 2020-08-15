class PlayerChar:  #naming Convention for class
    # Class object Attribute all objects can use this
    membership = True

    def __init__(self, name='anonymous', age=0):   # init is a magic method
        if (age>18):
            self._name = name
            self._age = age

    def shout(self):
       return print(f'My name is {self.name}')


player1 = PlayerChar('Puneeth',24)



print(player1._age) #Different memory locations suggests different objects
