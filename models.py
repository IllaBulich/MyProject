class Model:

    def __init__(self, name, description):
        self.__name = name
        self.__description = description

    @property
    def name(self):
        return self.__name

    @property
    def description(self):
        return self.__description


class Phone(Model):

    def __init__(self, name, os, description):
        super().__init__(name, description)
        self.__os = os

    def __str__(self):
        return F"марка {super().name}\nоперационная система {self.__os}\nописание поломки:\n{super().description}"


class Laptop(Model):

    def __init__(self, name, os, release, description):
        super().__init__(name, description)
        self.__os = os
        self.__release = release

    def __str__(self):
        return F"марка {super().name}\nоперационная система {self.__os}\nгод выпуска {self.__release}\nописание поломки:\n{super().description}"


class TV(Model):

    def __init__(self, name, diagonal, description):
        super().__init__(name, description)
        self.__diagonal = diagonal

    def __str__(self):
        return F"марка {super().name}\nдиагональ экрана {self.__diagonal}\nописание поломки:\n{super().description}"


tasc = Laptop("nameModel", " os", "release", " description")
