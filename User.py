import utils


class User:

    def __init__(self, login, password):
        self.__login = login
        self.__password = password

    def __str__(self):
        return f"логин {self.__login}|пароль {self.__password}"

    def examination(self, login, password):
        if self.__login == login and self.__password == password:
            return 1
        return 0

    @staticmethod
    def loginUs(login, password):
        for us in utils.user_list:
            if us == login and utils.user_list[us].examination(
                    login, password):
                return 1
        return 0

    @property
    def loginio(self):
        return self.__login

    @property
    def password(self):
        return self.__password