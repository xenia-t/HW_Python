# 1. Найти сумму чисел списка, стоящих на нечетной позиции
# Пример:[1,2,3,4] -> 4

import math
from ntpath import join
from random import randint, uniform

N = int(input('Введите длину списка: '))
random_list = [randint(1,100) for i in range(N)]
print(random_list)
sum = 0
for i in range(0, len(random_list), 2):
    sum += random_list[i]
print(f'Сумма чисел списка, стоящих на нечетной позиции = {sum}')


# 2.	Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д. 
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15] 

N = int(input('Введите длину списка: '))
random_list = [randint(1,10) for i in range(N)]
print(random_list)
result_list = []
for i in range(math.ceil(len(random_list)/2)):
    result_list.append(random_list[i]*random_list[-i-1])
print(result_list)

# 3. В заданном списке вещественных чисел найдите . 
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

N = int(input('Введите длину списка: '))
random_list = [round((uniform(1,10)),2) for i in range(N)]
print(random_list)
new_list = []
for i in range(len(random_list)):
    new_list.append(round((random_list[i]-int(random_list[i])),2))
print(new_list)
result = round((max(new_list) - min(new_list)),2)
print(f'Разница между максимальным и минимальным значением дробной части элементов = {result}')
    
# 4. Написать программу преобразования десятичного числа в двоичное

number = int(input('Введите число: '))
binary_number = []
while number != 0:
    binary_number.append(number % 2)
    number //= 2
binary_number.reverse()
result_number = int(''.join(map(str,(binary_number))))
print(result_number)

