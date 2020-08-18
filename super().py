class User():
    def __int__(self,email):
        self.email = email

    def sign_in(self):
        print('Logged in')


class Wizard(User):
    def __init__(self,name,power,email):
        super().__int__(email)
        self._name=name
        self._power=power

    def attack(self):
        print(f'Attacking with power of {self._power}')

class Archer(User):
    def __init__(self, name, num_arrows,email):
        super().__int__( email)
        self._name = name
        self._num_arrows = num_arrows

    def attack(self):
        print(f'Attacking with arrows: arrows left - {self._num_arrows}')



wizard1=Wizard('Puneeth',50,'puneethramchandra@gmail.com')
print(wizard1.email)
archer1=Archer('Robin',100,'Robin@gmail.com')
print(archer1.email)
