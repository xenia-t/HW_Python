# 1. Дан список чисел. Создать список в который попадают числа, описывающие возрастающую последовательность и содержащие максимальное количество элементов. 
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3, 4, 6, 7]
#  [5, 2, 3, 4, 6, 1, 7] => [2, 3, 4, 6, 7]
#  Порядок элементов менять нельзя

from random import randint

def LIS(list_numbers):
    lis = [0]*len(list_numbers)
    for i in range(len(list_numbers)):
        for j in range(i):
            if lis[j] >= lis[i] and list_numbers[j] < list_numbers[i]:
                lis[i]+=1

    max_value = max(lis)

    result_list = []
    for i in range(len(lis)-1,-1,-1):
        if max_value == lis[i]:
            result_list.append(list_numbers[i])
            max_value-=1

    result_list.reverse()
    return result_list

my_list = [1, 5, 2, 3, 4, 6, 1, 7]
print(LIS(my_list))

# # 2.	Создать и заполнить файл случайными целыми значениями. Выполнить сортировку содержимого файла по возрастанию. 

with open('file.txt', 'w') as file:
    for i in range(10):
        file.write(str(randint(1,500))+ ' ')

with open('file.txt', 'r') as file:
    data = list(map(int, file.read().split()))
    data.sort()

with open('file.txt', 'w') as file:
    file.write('\n')
    file.write(' '.join(map(str,data)))


# 3.	Вот вам файл с тысячей чисел. https://cloud.mail.ru/public/DQgN/LqoQzPEec
# Задача: найти триплеты и просто выводить их на экран. Триплетом называются три числа, которые в сумме дают 0. 
# (решение будет долгим, ибо является демонстрационным при теме многопоточного программирования). 

with open('1Kints.txt', 'r') as file:
    listnum = list(map(int, file.readlines()))

count = 0
for i in range( 0, len(listnum)-2):
    for j in range(i + 1, len(listnum)-1):
        for k in range(j + 1, len(listnum)):
            if (listnum[i] + listnum[j] + listnum[k] == 0):
                print('Триплет: ', listnum[i], ' + ', listnum[j], ' + ', listnum[k], '= 0') 
                count += 1
print(f'Количество триплетов из уникальных комбинаций = {count}')

