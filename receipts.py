import datetime
import models
from random import randint


class Receipts:

    def __init__(self, surname, name, patronymic, model):
        self.__receiptNumber = randint(1, 99999)
        self.__model = model
        self.__date1 = datetime.date.today()
        self.__dateFinih = self.__date1 + datetime.timedelta(
            days=randint(1, 5))
        self.__fio = surname + " " + name + " " + patronymic
        self.__status = "ремонтируется"

    def __str__(self):
        return f"номер квитанции {self.__receiptNumber}\nФИО {self.__fio}\nтип изделия\n{self.__model}\nдата приемки {self.__date1}\nдата выполнения ремонта {self.__dateFinih}\nстатус {self.__status}"

    def setStatus(self, status):
        self.__status = status

    def setDateFinih(self, date):
        self.__dateFinih = date

    @property
    def fio(self):
        return self.__fio

    @property
    def receiptNumber(self):
        return self.__receiptNumber
