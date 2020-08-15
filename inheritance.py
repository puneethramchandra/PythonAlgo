class User():
    def sign_in(self):
        print('Logged in')


class Wizard(User):
    def __init__(self,name,power):
        self._name=name
        self._power=power

    def attack(self):
        print(f'Attacking with power of {self._power}')

class Archer(User):
    def __init__(self, name, num_arrows):
        self._name = name
        self._num_arrows = num_arrows

    def attack(self):
        print(f'Attacking with arrows: arrows left - {self._num_arrows}')



wizard1=Wizard('Puneeth',50)
archer1=Archer('Robin',100)


print(isinstance(wizard1, User))


wizard1.attack()
archer1.attack()
wizard1.sign_in()