"""System module."""
import datetime
from random import randint


class Receipts:
    """A dummy docstring."""

    def __init__(self, surname, name, patronymic, model):
        self.__receipt_number = randint(1, 99999)
        self.__model = model
        self.__date1 = datetime.date.today()
        self.__date_finih = self.__date1 + datetime.timedelta(
            days=randint(1, 5))
        self.__fio = surname + " " + name + " " + patronymic
        self.__status = "ремонтируется"

    def __str__(self):
        str1 = f"номер квитанции {self.__receipt_number}\nФИО {self.__fio}\n"
        str2 = f"тип изделия\n{self.__model}\nдата приемки {self.__date1}\n"
        str3 = f"дата выполнения ремонта {self.__date_finih}\nстатус {self.__status}"
        return str1 + str2 + str3

    def set_status(self, status):
        """A dummy docstring."""
        self.__status = status

    def set_date_finih(self, date):
        """A dummy docstring."""
        self.__date_finih = date

    @property
    def fio(self):
        """A dummy docstring."""
        return self.__fio

    @property
    def receipt_number(self):
        """A dummy docstring."""
        return self.__receipt_number
