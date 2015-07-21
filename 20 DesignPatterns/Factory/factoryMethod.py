__author__ = 'adelli'

class Dog:

    ''' A simple Dog Class'''

    def __init__(self,name):
        self.name = name

    def speak(self):
        return 'Woof!'

class Cat:

    ''' A simple Cat Class'''

    def __init__(self,name):
        self.name = name

    def speak(self):
        return 'Meow!'


def get_pet(pet='dog'):

    '''
    :param pet: string
    :return: pet Object
    '''

    pets = dict(dog=Dog("Hope"), cat=Cat("Peace"))

    return pets[pet]

d = get_pet('dog')

print(d.speak())

c = get_pet('cat')

print(c.speak())