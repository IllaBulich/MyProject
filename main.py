from models import Laptop, Phone, TV
import receipts
import utils

while True:
    print("1-сдать в ремонт")
    print("2-просмотреть информацию")
    i = utils.getNumber(1, 3)

    if i == 1:

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
        utils.rec[buf.receiptNumber] = buf

    elif i == 2:

        print("1-Поиск по номеру квитанции")
        print("2-Поиск по ФИО")
        i = utils.getNumber(1, 3)
        if i == 1:
            
            print("Поиск по номеру квитанции")
            receiptNumber = utils.getNumber(1, 99999)
            if receiptNumber in utils.rec:
                print(utils.rec[receiptNumber])
            else:
                print("чек не найден")

        elif i == 2:
            
            print("Поиск по ФИО")
            surname = input("Введите фамилию: ")
            name = input("Введите имя: ")
            patronymic = input("Введите очество: ")
            for receipts in utils.rec.values():
                if receipts.fio == f"{surname} {name} {patronymic}":
                    print(receipts)
                    
