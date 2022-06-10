# 1. Найти НОК двух чисел

from cmath import sqrt
from random import randint


def gcd(x, y):
    while x != 0 and y != 0:
        if x >= y:
            x %= y
        else:
            y %= x
    return x or y

number1 = int(input('Введите первое число: '))
number2 = int(input('Введите второе число: '))

print(f'НОК чисел {number1} и {number2} = {(number1*number2)//gcd(number1,number2)}')    



# 2.	Вычислить число Пи c заданной точностью d
# Пример: при d = 0.001,  c= 3.141. 

# The Gregory series

d = float(input('Введите точность для числа Пи: '))
n=0
top_row=0
bot_row=0
 
while True: 
    n +=1
    top_row=(bot_row+4/(2*n-1))
    n +=1
    bot_row=(top_row-(4/(2*n-1)))

    if ((top_row-bot_row) <= d):
        break 

Pi=(top_row+bot_row)/2
print (Pi)


# 3. Составить список простых множителей натурального числа N

N = int(input('Введите число: '))
prime_factors = []
i = 2
while i <= (int(sqrt(N))):
    if N % i == 0:
        prime_factors.append(i)
        N//=i
    else:
        i+=1
if N > 1:
    prime_factors.append(N)
print(f'Простые множители числа {N}: {prime_factors}')

# 4.	Дана последовательность чисел. Получить список неповторяющихся элементов исходной последовательности
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]

mylist = [1, 2, 3, 5, 1, 5, 3, 10]
reslist = []
for num in mylist:
    if num not in reslist:
        reslist.append(num)
print(reslist)

# 5. Дан текстовый файл, содержащий целые числа. Удалить из него все четные числа. 

with open('file.txt', 'w') as file:
    for i in range(10):
        file.write(str(randint(1,500))+ ' ')

with open('file.txt', 'r') as file:
    data = list(map(int, file.read().split()))
            

with open('file.txt', 'a') as file:
    file.write('\n')
    file.write(' '.join(map(str,[num for num in data if num % 2])))