from random import randint as randint_std
from pet_class import Pet as Pet_imported

class Dog(Pet_imported):
    """ Pies """
    def __init__(self, name='Nori', age=randint_std(1,20)):
        """ Inicjacja atrybutow """
        super().__init__(name, age)

    def sit(self):
        """ Symulacja siedzenia """
        print(f'{self.name.title()} siedzi')

    def roll_over(self):
        """ Symulacja lezenia na plecach """
        print(f'{self.name.title()} lezy na plecach')
