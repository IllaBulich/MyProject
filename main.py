from models import Laptop, Phone, TV
import receipts
import utils
from collections import Counter


rec =dict()

while True:
    surname = input("Введите фамилию: ")
    name = input("Введите имя: ")
    patronymic = input("Введите очество: ")

    print("1-телефон\n2-ноутбук\n3-телевизор")
    i = utils.getNumber(1, 3)

    nameModel = input("Введите название марки: ")

    if i == 1:
        os = input("Какая операционная система на устройстве: ")
        description = input("Опесание неисправности: ")
        tasc = Phone(nameModel, os, description)
    if i == 2:
        os = input("Какая операционная система на устройстве: ")
        release = input("Год выпуска: ")
        description = input("Опесание неисправности: ")
        tasc = Laptop(nameModel, os, release, description)
    if i == 3:
        diagonal = input("Диагональ экрана: ")
        description = input("Опесание неисправности: ")
        tasc = TV(nameModel, diagonal, description)

    buf = receipts.Receipts(surname, name, patronymic, tasc)
    rec[buf.fio]=buf

    for i in rec:
        print(rec[i])
