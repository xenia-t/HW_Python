# 1. Напишите программу, удаляющую из текста все слова содержащие "абв", которое регистронезависимо. Используйте знания с последней лекции. Выполните ее в виде функции. 
# Пример: «абвгдеж рабав копыто фабв Абкн абрыволк аБволк»

inp_text = 'абвгдеж рабав копыто фабв Абкн абрыволк аБволк'

fragment = 'абв'

inp_text = list(filter(lambda word: fragment not in word, inp_text.split()))
res = " ".join(inp_text)
print (res)

# 2. Вы когда-нибудь играли в игру "Крестики-нолики"? Попробуйте создать её, причем чтобы сыграть в нее можно было в одиночку. 

#Крестики-Нолики

import random


def instruction():
    print(
"""
Игра "Крестики и нолики"

Введите цифру от 1 до 9, чтобы сделать свой ход.

Числа соответсвуют полям доски:

1 | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9
\n
"""
        )

def Board(board): # Отображение игровой доски с выполненными ходами
    print("\n\t", board[1], "|", board[2],"|",board[3])
    print("\t",  "---------")
    print("\n\t", board[4], "|", board[5],  "|", board[6])
    print("\t",  "---------")
    print("\n\t", board[7], "|", board[8],  "|",  board[9],"\n")

def input_player_symbol(): # Выбор символа игроком (Х или О)
    symb = ''
    while not (symb == 'Х' or symb == 'О'):
        print('Каким символом вы хотите играть: Х или О?')
        symb = input().upper()

    if symb == 'Х':
        return ['Х', 'О']
    else:
        return ['О', 'Х']

def who_first(): #Определение первого хода
    if random.randint(0, 1) == 0:
        return 'компьютер'
    else:
        return 'игрок'

def play_again(): 
    print('Вы хотите сыграть еще раз? (да или нет)')
    return input().lower().startswith('д')

def win_game(board, marker): # Возврат выигрышных позиций: верхняя, средняя, нижняя, левая вертикальная, 
    # центральная вертикальная, правая вертикальная линии и 2 диагонали соответственно
    return ((board[1] == marker and board[2] == marker and board[3] == marker) or 
            (board[4] == marker and board[5] == marker and board[6] == marker) or 
            (board[7] == marker and board[8] == marker and board[9] == marker) or 
            (board[1] == marker and board[4] == marker and board[7] == marker) or 
            (board[2] == marker and board[5] == marker and board[8] == marker) or 
            (board[3] == marker and board[6] == marker and board[9] == marker) or 
            (board[3] == marker and board[5] == marker and board[7] == marker) or 
            (board[1] == marker and board[5] == marker and board[9] == marker)) 

 
def copy_board(board): # Возврат копии доски
    copy_bo = []
    for slot in board:
        copy_bo.append(slot)
    return copy_bo
 
def potential_move(board): # Возврат списка всех доступных ходов
    free_moves = []
    for i in range(1, 10):
        if board[i] == ' ':
            free_moves.append(i)
    return(free_moves)
 
def player_move(board): # Ход игрока
    move = ' '
    print('Ваш ход. Введите номер от 1 до 9: ')
    while move not in potential_move(board):
        move = ' '
        while move not in range(1,10):
            move = int(input())
        if move not in potential_move(board):
            print('Поле занято. Введите другой номер: ')
    return (move)
    

def computer_move(board, computer_symb, player_symb): # Ход компьютера

    print('\nХод компьютера: ')
    copy = copy_board(board)
    for i in potential_move(copy):
        copy[i] = computer_symb
        if win_game(copy, computer_symb):
            print(i)
            return i
        copy[i]= ' '

    for j in potential_move(board):
        copy[j]=player_symb
        if win_game(copy,player_symb):
            print(j)
            return j
        copy[j]=' '
    
    for k in potential_move(board):
        print(k)
        return k

 
def not_potential_moves(board): # 
    if potential_move(board):
        return False
    return True


instruction()

while True: # Основная часть
    current_board = [' ']*10
    player_symb, computer_symb = input_player_symbol()
    who = who_first()
    print ('Первым будет ходить '+who +'\n')
    playing = True
 
    while playing:
        if who == 'игрок':
            Board(current_board)
            move = player_move(current_board)
            current_board[move]=player_symb
            if win_game(current_board, player_symb):
                Board(current_board)
                print ('Вы победили!')
                playing = False
            else:
                if not_potential_moves(current_board):
                    Board(current_board)
                    print('Ничья.')
                    break
                else:
                    who = 'компьютер'
        else:
            move=computer_move(current_board,computer_symb, player_symb)
            current_board[move]=computer_symb
            if win_game(current_board, computer_symb):
                Board(current_board)
                print('Вы поиграли:(')
                playing = False
            else:
                if not_potential_moves(current_board):
                    Board(current_board)
                    print('Ничья.')
                    break
                else:
                    who = 'игрок'

    if not play_again():
        break



# 3. Вот вам текст:
# «Ну, вышел я, короче, из подъезда. В общем, короче говоря, шел я, кажется, в магазин. Ну,эээ, в общем, было лето, кажется. Как бы тепло. 
# Солнечно, короче. Иду я, иду, в общем, по улице, а тут, короче, яма. Я, эээээ.... Упал в нее. И снова вышел, короче, из подъезда. Ясен пень, в магазин. 
# В общем, лето на дворе, жарко, солнечно, птицы, короче, летают. Кстати, иду я по улице, иду, а тут, короче, яма. Ну, я в нее упал, в общем. 
# Вышел из подъезда, короче. Лето на дворе, ясен пень. Птицы поют, короче, солнечно. В общем, в магазин мне надо. Что-то явно не так, короче. «Рекурсия», - подумал я. 
# Ээээ...короче, в общем, пошел другой дорогой и не упал в эту... ээээ... яму. Хлеба купил».
# Отфильтруйте его, чтобы этот текст можно было нормально прочесть. Предусмотрите вариант, что мусорные слова могли быть написаны без использования запятых.

# from operator import index
# import re
# import string


text = 'Ну, вышел я, короче, из подъезда. В общем, короче говоря, шел я, кажется, в магазин. Ну,эээ, в общем, было лето, кажется. Как бы тепло. Солнечно, короче. Иду я, иду, в общем, по улице, а тут, короче, яма. Я, эээээ.... Упал в нее. И снова вышел, короче, из подъезда. Ясен пень, в магазин. В общем, лето на дворе, жарко, солнечно, птицы, короче, летают. Кстати, иду я по улице, иду, а тут, короче, яма. Ну, я в нее упал, в общем. Вышел из подъезда, короче. Лето на дворе, ясен пень. Птицы поют, короче, солнечно. В общем, в магазин мне надо. Что-то явно не так, короче. «Рекурсия», - подумал я. Ээээ...короче, в общем, пошел другой дорогой и не упал в эту... ээээ... яму. Хлеба купил'
trash_words = ['ну', 'В общем', 'короче говоря', 'кажется', 'иду я','ээ','э' ,'короче,', 'кажется', 'в общем', 'ясен пень', 'как бы', 'кстати', 'короче', ', ,', '....', '...']


for words in trash_words:
    text = text.casefold().replace(words, '').replace(',  ', ' ').replace(', .', '.')


sentences = text.split('.')

final_sentences = []
for sentence in sentences:
    sentence = sentence.lstrip(' ,').rstrip(',').strip()
    if not sentence:
        continue

    sentence = sentence.capitalize()
    final_sentences.append(sentence)

final_text = '. '.join(final_sentences)
final_text = final_text  + '.'


print(final_text)
