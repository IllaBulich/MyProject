"""System module."""


class Model:
    """A dummy docstring."""

    def __init__(self, name, description):
        self.__name = name
        self.__description = description

    @property
    def name(self):
        """A dummy docstring."""
        return self.__name

    @property
    def description(self):
        """A dummy docstring."""
        return self.__description


class Phone(Model):
    """A dummy docstring."""

    def __init__(self, name, os, description):
        super().__init__(name, description)
        self.__os = os

    def __str__(self):
        str1=f"марка {super().name}\nоперационная система {self.__os}\n"
        str2=f"описание поломки:\n{super().description}"
        return str1 + str2


class Laptop(Model):
    """A dummy docstring."""

    def __init__(self, name, os, release, description):
        super().__init__(name, description)
        self.__os = os
        self.__release = release

    def __str__(self):
        str1 = f"марка {super().name}\nоперационная система {self.__os}\n"
        str2 = f"год выпуска {self.__release}\nописание поломки:\n{super().description}"
        return str1 + str2


class TV(Model):
    """A dummy docstring."""

    def __init__(self, name, diagonal, description):
        super().__init__(name, description)
        self.__diagonal = diagonal

    def __str__(self):
        str1 = f"марка {super().name}\nдиагональ экрана {self.__diagonal}\n"
        str2 = f"описание поломки:\n{super().description}"
        return str1 + str2


tasc = Laptop("nameModel", " os", "release", " description")
