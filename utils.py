"""System module."""
import pickle

FILENAME1 = "Receipts.dat"
FILENAME2 = "User.dat"


rec = {}
user_list = {}


with open(FILENAME1, "rb") as file:
    rec = pickle.load(file)
with open(FILENAME2, "rb") as file:
    user_list = pickle.load(file)


def rec_seve():
    """A dummy docstring."""
    with open(FILENAME1, "wb") as file:
        pickle.dump(rec, file)


def user_list_seve():
    """A dummy docstring."""
    with open(FILENAME2, "wb") as file:
        pickle.dump(user_list, file)



def get_number(_min=0, _max=1000000):
    """A dummy docstring."""
    while True:
        number = input('Введите целое положительное число: ')
        if number.isdigit() and _min <= int(number) <= _max:
            return int(number)


# tasc = Phone(1, 1, 1)
# buf = receipts.Receipts("Будич", 'Илья', 'Олегович', tasc)
# rec[buf.receipt_number] = buf
# tasc = Phone(2, 2, 2)
# buf = receipts.Receipts('Будич', 'Илья', 'Олегович', tasc)
# rec[buf.receipt_number] = buf
# tasc = Phone(3, 3, 3)
# buf = receipts.Receipts('Бобрик', 'Михаиль', 'Михайлович', tasc)
# rec[buf.receipt_number] = buf
# tasc = Phone(7, 7, 7)
# buf = receipts.Receipts('Петров', 'Пётар', 'Петрович', tasc)
# rec[buf.receipt_number] = buf
# tasc = Phone(7, 7, 7)
# buf = receipts.Receipts('Бобрик', 'Пётар', 'Олегович', tasc)
# rec[buf.receipt_number] = buf

# buf = User("1", "1")
# utils.user_list[buf.loginio] = buf
# buf = User("user", "1234")
# utils.user_list[buf.loginio] = buf
# buf = User("likol", "likol")
# utils.user_list[buf.loginio] = buf
