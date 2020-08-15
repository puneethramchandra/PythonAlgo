
class Cat:
    species = 'mammal'
    
    def __init__(self, name, age):
        self.name = name
        self.age = age


cat1 = Cat('Pun', 4)
cat2 = Cat('Ram', 5)
cat3 = Cat('Chan', 6)


def oldest_cat(*ages):

    oldest=max(*ages)

    return oldest


print(f'The oldest cat is {oldest_cat(cat1.age,cat2.age,cat3.age)} years old')