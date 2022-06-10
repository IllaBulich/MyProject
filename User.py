"""System module."""
import utils


class User:
    """A dummy docstring."""

    def __init__(self, login, password):
        self.__login = login
        self.__password = password

    def __str__(self):
        return f"логин {self.__login}|пароль {self.__password}"

    def examination(self, login, password):
        """A dummy docstring."""
        if self.__login == login and self.__password == password:
            return 1
        return 0

    @staticmethod
    def login_user(login, password):
        """A dummy docstring."""
        for key in utils.user_list:
            if key == login and utils.user_list[key].examination(
                    login, password):
                return 1
        return 0

    @property
    def loginio(self):
        """A dummy docstring."""
        return self.__login

    @property
    def password(self):
        """A dummy docstring."""
        return self.__password
