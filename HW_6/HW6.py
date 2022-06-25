# 1 -  Написать программу вычисления арифметического выражения заданного строкой. Используются операции +,-,/,*. приоритет операций стандартный. Функцию eval не использовать!
# Пример: 2+2 => 4; 1+2*3 => 7; 1-2*3 => -5;
# Дополнительно: Добавить возможность использования скобок, меняющих приоритет операций. 
# Пример: 1+2*3 => 7; (1+2)*3 => 9;


from audioop import reverse


input_prob = input('Введите арифметическое выражение: ')
ops = {'+':2, '-':2, '/':1, '*':1}

def rpn(input_prob): # обработка выражения - формирование списка постфиксной записи (обратная польская нотация)
    stack, reverse_polish_prob, digit = [], [], False
    for symb in input_prob:
        if symb in '0123456789':
            if len(reverse_polish_prob) == 0:
                reverse_polish_prob = [symb] + reverse_polish_prob
            else:
                if reverse_polish_prob[0][-1] in '0123456789' and digit: 
                    reverse_polish_prob[0] += symb
                else: 
                    reverse_polish_prob = [symb] + reverse_polish_prob
            digit = True
        else: 
            digit = False
    
        if symb == '(':
            stack = [symb] + stack
    
        if symb == ')':
            while stack != [] and stack[0] != '(': 
                reverse_polish_prob, stack = [stack[0]] + reverse_polish_prob, stack[1:]
            if stack != [] and stack[0] == '(': 
                stack = stack[1:]
    
        if symb in ops:
            while stack != [] and stack[0] in ops and ops[symb] >= ops[stack[0]]: 
                reverse_polish_prob, stack = [stack[0]] + reverse_polish_prob, stack[1:]
            stack = [symb] + stack

    while stack != []: 
        reverse_polish_prob, stack = [stack[0]] + reverse_polish_prob, stack[1:]

    reverse_polish_prob.reverse()
    return(reverse_polish_prob)

print('\nинфиксная запись:' , (input_prob))
print('постфиксная запись (RPN)', rpn(input_prob))


def rpn_calc(RPN): # вычисление арифметического выражения 
    result=[]
    for symb in RPN:
        if symb.isdigit():
            result.append(float(symb))
        else:
            a2=result.pop()
            a1=result.pop()
            if symb=='+':
                result.append(a1+a2)
            if symb=='-':
                result.append(a1-a2)
            if symb=='*':
                result.append(a1*a2)
            if symb=='/':
                result.append(a1/a2)
    return result.pop()            

print(f'\n{input_prob} = {rpn_calc(rpn(input_prob))}')


# 2 - Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных файлах 
# (в одном файлике отрывок из какой-то книги, а втором файлике — сжатая версия этого текста). 

def encode_message(data):
    encode = ''
    previous_symb = ''
    count = 1

    if not data: return ''

    for symb in data:
        if symb != previous_symb:
            if previous_symb:
                encoding += str(count) + previous_symb
            count = 1
            previous_symb = symb
        else:
            count += 1
    else:
        encode += str(count) + previous_symb
        return encode

def decode_message(gdg):
    decode = ''
    count = ''
    for symb in gdg:
        if symb.isdigit():
            count += symb
        else:
            decode += symb * int(count)
            count = ''
    return decode


with open('input.txt', 'r', encoding='utf-8') as data_input, open('output.txt', 'w', encoding='utf-8') as data_output:
    text = data_input.read()
    data_output.write(encode_message(text))



# with open('output.txt', 'r', encoding='utf-8') as data_input, open('input.txt', 'w', encoding='utf-8') as data_output:
#     text = data_input.read()
#     data_output.write(decode_message(text))



# 3 -  ROT13 - это простой шифр подстановки букв, который заменяет букву буквой, которая идет через 13 букв после нее в алфавите. ROT13 является примером шифра Цезаря.
# Создайте функцию, которая принимает строку и возвращает строку, зашифрованную с помощью Rot13 . Если в строку включены числа или специальные символы, 
# они должны быть возвращены как есть. Также создайте функцию, которая расшифровывает эту строку обратно (некий начальный аналог шифрования сообщений). 
# Не использовать функцию encode.

def rot13(massage):
    result_massage = ''
    for symbol in massage:
        if (symbol >= 'A' and symbol <= 'M') or (symbol >= 'a' and symbol <= 'm'):
            result_massage += chr(ord(symbol)+13)
        elif (symbol >= 'N' and symbol <= 'Z') or (symbol >= 'n' and symbol <= 'z'):
            result_massage += chr(ord(symbol)-13)
        else:
            result_massage += symbol
    return result_massage
    
print (rot13('ABCDEFGHIJKLMNO190PQRSTUVWXY27Zabcdefghijklmnopqrstuvwxyz 55'))
