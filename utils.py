"""System module."""
from models import Phone
import receipts
import User

rec = {}
user_list = {}

tasc = Phone(1, 1, 1)
buf = receipts.Receipts("Будич", 'Илья', 'Олегович', tasc)
rec[buf.receipt_number] = buf
tasc = Phone(2, 2, 2)
buf = receipts.Receipts('Будич', 'Илья', 'Олегович', tasc)
rec[buf.receipt_number] = buf
tasc = Phone(3, 3, 3)
buf = receipts.Receipts('Бобрик', 'Михаиль', 'Михайлович', tasc)
rec[buf.receipt_number] = buf
tasc = Phone(7, 7, 7)
buf = receipts.Receipts('Петров', 'Пётар', 'Петрович', tasc)
rec[buf.receipt_number] = buf
tasc = Phone(7, 7, 7)
buf = receipts.Receipts('Бобрик', 'Пётар', 'Олегович', tasc)
rec[buf.receipt_number] = buf

buf = User.User("admin", "admin")
user_list[buf.loginio] = buf
buf = User.User("user", "1234")
user_list[buf.loginio] = buf
buf = User.User("likol", "likol")
user_list[buf.loginio] = buf


def get_number(_min=0, _max=1000000):
    """A dummy docstring."""
    while True:
        number = input('Введите целое положительное число: ')
        if number.isdigit() and _min <= int(number) <= _max:
            return int(number)
