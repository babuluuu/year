
result = 0
print ("Введите 1 число ")
number1 = int(input())
print ("Введите 2 число ")
number2 = int(input())
numbercommand = input ("Какую опреацию: \n1. + \n2. - \n3./\n4.*\n5.^")
if numbercommand == '1':
    result = number1 + number2
    print (f"Результат сложения:{result}")
elif numbercommand == '2':
    result = number1 - number2
    print (f"Результат вычитания:{result}")
elif numbercommand == '3':
    if number2 !=0:
        result = number1/number2
        print (f"Результат деления :{result}")
    else:
        print ("Нельзя делить на 0:")
elif numbercommand == '4':
    result = number1 * number2
    print (f"Результат умножения:{result}")
elif numbercommand == '5':
    result = number1 ** number2
    print (f"Результат возведения в степень:{result}")

while True :
    print ("Введите следующее число:")
    number3 = int(input())
    numbercommand = input ("Какую опреацию: \n1. + \n2. - \n3./\n4.*\n5.^")
    if numbercommand == '1':
        result = number3 + result
        print (f"Результат сложения:{result}")
    elif numbercommand == '2':
        result = result - number3
        print (f"Результат вычитания:{result}")
    elif numbercommand == '3':
        if number3 !=0:
            result = number3/result
            print (f"Результат деления :{result}")
        else:
            print ("Нельзя делить на 0:")
        
    elif numbercommand == '4':
        result = result * number3
        print (f"Результат умножения:{result}")
    elif numbercommand == '5':
        result = result ** number3
        print (f"Результат возведения в степень:{result}")

    


