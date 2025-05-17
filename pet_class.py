class Pet:
    """ Zwierze """
    def __init__(self, name, age=1):
        """ Inicjacja atrybutow """
        self.name=name
        self.age=age

    def __repr__(self):
        """ Opisanie siebie """
        return f'{self.name.title()}{{age:{self.age}}}'

    def eat(self):
        """ Symulacja jedzenia """
        print(f'{self.name.title()} je')
