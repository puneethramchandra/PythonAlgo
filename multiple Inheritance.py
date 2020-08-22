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

    def check_arrows(self):
        print(f' {self._num_arrows} remaining')

    def run(self):
        print('ran really fast')


class HybridBorg( Wizard,Archer):
    def __init__(self,name,power,num_arrows):
        Archer.__init__(self,name,num_arrows)
        Wizard.__init__(self,name,power)

hb1= HybridBorg('Puneeth',10,100)

print(hb1.sign_in())


print(hb1.attack())
print(hb1.check_arrows())


print(HybridBorg.__mro__)   #Method Resolution Order