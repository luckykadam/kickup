class Entity:
    def __str__(self):
        return ', '.join(['{}: {}'.format(attribute, value) for attribute, value in self.__dict__.items()])


class User(Entity):
    def __init__(self, id, name):
        self.id = id
        self.name = name


class Group(Entity):
    def __init__(self, id, name):
        self.id = id
        self.name = name
