__author__ = 'adelli'


class Dog:
    '''One of the objects to be return'''

    def speak(self):
        return 'Woof'

    def __str__(self):
        return 'Dog'

class DogFactory:
    '''Concrete Dog Factory'''

    def get_pet(self):
        '''Returns a Dog Object '''
        return Dog()

    def get_food(self):
        '''returns a food'''
        return 'Dog food'

class PetStore:
    ''' PetStore houses our abstract class'''

    def __init__(self, pet_factory=None):
        self._pet_factory = pet_factory

    def show_pet(self):
        '''Utility method to display the details of the objects returned by the DogFactory'''
        pet = self._pet_factory.get_pet()
        food = self._pet_factory.get_food()

        print("Our Pet is '{}'".format(pet))
        print("Our Pet says hello by saying '{}'".format(pet.speak()))
        print("Its food is '{}'".format(food))


#  Create a concrete factory

godF = DogFactory()

#  Create a pet store housing our abstract Factory

pet_store = PetStore(godF)

# Invoke the utility method to shopw the details of our pets

pet_store.show_pet()