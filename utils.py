from models import  Phone
import receipts

rec = dict()

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

def getNumber(min=0, max=1000000):
    while True:
        getNumber = input('Введите целое положительное число: ') 
        if getNumber.isdigit() and min<=int(getNumber)<=max : return int(getNumber)
        
