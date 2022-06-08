from models import Laptop, Phone, TV
import datetime
import receipts
import utils
import User

while True:
    print("1-сдать в ремонт")
    print("2-просмотреть информацию")
    print("3-зайти в администраторскую панель")
    print("4-выход")
    i = utils.getNumber(1, 4)

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

    elif i == 3:
        login = input("Введите логин: ")
        password = input("Введите пароль: ")
        if User.User.loginUs(login, password):
            while True:
                print("1-Действия с админами")
                print("2-Действия с квитанциями")
                print("3-выход")

                i = utils.getNumber(1, 3)
                print("\n")
                if i == 1:
                    while True:
                        for us in utils.user_list:
                            print(utils.user_list[us])

                        print("1-удалить админа из списка")
                        print("2-добавить нового админа ")
                        print("3-выход")
                        i = utils.getNumber(1, 3)

                        if i == 1:
                            login = input(
                                "Введите логин админа для удаления: ")
                            utils.user_list.pop(login, 1)

                        elif i == 2:
                            login = input("Введите логин: ")
                            password = input("Введите пароль: ")
                            buf = User.User(login, password)
                            utils.user_list[buf.loginio] = buf

                        elif i == 3:
                            break

                elif i == 2:
                    for us in utils.rec:
                        print(us)
                    print("Поиск по номеру квитанции")
                    receiptNumber = utils.getNumber(1, 99999)
                    if receiptNumber in utils.rec:
                        while True:
                            print(utils.rec[receiptNumber])
                            print("1-изменить статус ремонта")
                            print("2-изменить дату выполнения ремонта")
                            print("3-выход")
                            i = utils.getNumber(1, 3)

                            if i == 1:
                                status = input(
                                    "Введите новый статус ремонта: ")
                                utils.rec[receiptNumber].setStatus(status)

                            elif i == 2:
                                date = input('Дата (mm/dd/yyyy): ')
                                try:
                                    valid_date = datetime.datetime.strptime(
                                        date, '%m/%d/%Y').date()
                                    utils.rec[receiptNumber].setDateFinih(
                                        valid_date)
                                except ValueError:
                                    print('Invalid date!')

                            elif i == 3:
                                break

                    else:
                        print("чек не найден")

                elif i == 3:
                    break

        else:
            print("неверный логин или пароль")

    elif i == 4:
        break
