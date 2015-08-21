__author__ = 'adelli'


class Component(object):
    '''Abstract Class'''

    def __init__(self, *args, **kwargs):
        pass

    def component_action(self):
        pass


class Child(Component):
    '''Child Class'''



    def __init__(self, *args, **kwargs):
        Component.__init__(self, *args, **kwargs)
        self.name = args[0]

    def component_action(self):
        print("{}".format(self.name))


class Composite(Component):
    '''Composite Class'''


    def __init__(self, *args, **kwargs):
        Component.__init__(self, *args, **kwargs)
        self.name = args[0]
        self.children = []

    def component_action(self):
        print("{}".format(self.name))

        for child in self.children:
            child.component_action()

    def append_child(self, component):
        self.children.append(component)

    def remove_child(self, component):
        self.children.remove(component)

# build a composite submenu
sub1 = Composite("submenu 1")

# create a new child submenu 11
sub11 = Child('submenu 11')

# create a new child submenu 11
sub12 = Child('submenu 12')

sub1.append_child(sub11)

sub1.append_child(sub12)

# build a composite seubmenu
top = Composite("top_menu")

sub2 = Child("submenu2")

top.append_child(sub2)
top.append_child(sub1)

top.component_action()