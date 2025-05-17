from classes.cat_class import Cat
from classes.dog_class import Dog

my_pets=(Cat('Milunia', 18), Dog(), Cat('Rudy', 8), Dog('Dasza', 4),
        Cat('Kot', 2))

print(f'Moje zwierzeta po kolei: {my_pets}')

my_cats=[]
my_dogs=[]
for pet in my_pets:
    if isinstance(pet, Dog):
        my_dogs.append(pet)
    elif isinstance(pet, Cat):
        my_cats.append(pet)

print(f'Moje najnowsze zwierze: {my_pets[-1]}')
print(f'Moje srodkowe zwierze: {my_pets[int(len(my_pets)/2)]}')
print(f'Moje najstarsze zwierze: {my_pets[0]}')

print(f'Moje psy: {my_dogs}')
print(f'Moje koty: {my_cats}')

my_dogs[-2].sit()
my_cats[-1].purr()
last_pet=my_cats[-1]
try:
    last_pet.roll_over()
except AttributeError:
    print(f'Ostatnie zwierze {last_pet} niestety nigdy nie nauczy sie lezec na plecach')
