
def getNumber(min=0, max=1000000):
    while True:
        getNumber = input('Введите целое положительное число: ') 
        if getNumber.isdigit() and min<=int(getNumber)<=max : return int(getNumber)
        
