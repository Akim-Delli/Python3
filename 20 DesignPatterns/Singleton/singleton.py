__author__ = 'adelli'

class Borg:
    '''Borg class making class attribute global'''
    _shared_state ={}

    def __init__(self):
        self.__dict__ = self._shared_state # Make it an attribute dictionary

class Singleton(Borg): # Inherits from the Borg class
    '''This class now shares all its attributes among its various instances'''
    # this essential makes the singleton object an object oriented global variable

    def __init__(self, **kwargs):
        self._shared_state.update(kwargs)

    def __str__(self):
        # Returns the attribute dictionary for printing
        return str(self._shared_state)

x = Singleton(http = "Hyper Text Protocol")
print(x)

y = Singleton(SNMP = "Simple Network Management Protocol")
print(y)