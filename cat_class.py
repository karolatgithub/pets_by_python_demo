from pet_class import Pet as Pet_imported

class Cat(Pet_imported):
    """ Kot """

    def purr(self):
        """ Symulacja mruczenia """
        print(f'{self.name.title()} mruczy')
