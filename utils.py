from models import Phone
import receipts
import User

rec = dict()

user_list = dict()

tasc = Phone(1, 1, 1)
buf = receipts.Receipts("Будич", 'Илья', 'Олегович', tasc)
rec[buf.receiptNumber] = buf
tasc = Phone(2, 2, 2)
buf = receipts.Receipts('Будич', 'Илья', 'Олегович', tasc)
rec[buf.receiptNumber] = buf
tasc = Phone(3, 3, 3)
buf = receipts.Receipts('Бобрик', 'Михаиль', 'Михайлович', tasc)
rec[buf.receiptNumber] = buf
tasc = Phone(7, 7, 7)
buf = receipts.Receipts('Петров', 'Пётар', 'Петрович', tasc)
rec[buf.receiptNumber] = buf
tasc = Phone(7, 7, 7)
buf = receipts.Receipts('Бобрик', 'Пётар', 'Олегович', tasc)
rec[buf.receiptNumber] = buf

buf = User.User("admin", "admin")
user_list[buf.loginio] = buf
buf = User.User("user", "1234")
user_list[buf.loginio] = buf
buf = User.User("likol", "likol")
user_list[buf.loginio] = buf


def getNumber(min=0, max=1000000):
    while True:
        getNumber = input('Введите целое положительное число: ')
        if getNumber.isdigit() and min <= int(getNumber) <= max:
            return int(getNumber)
