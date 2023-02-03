print("ПРАКТИЧЕСКАЯ РАБОТА №2")
while True:
    n = int(input())
    N = 1
    sum = 0
    for a in range(1, n+1):
        for b in range(1, a+1):
            N = N * b
        sum += N
    print(sum) 
    year = int(input("Введите год: "))
    if(year%4==0 and year%100!=0 or year%400==0):
        print("Это високосный год")      
        print("Сумма всех чисел: ", b)
    else:
        print("Это невисокосный год")
        print("Сумма всех чисел: ", b)

         
