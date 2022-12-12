import shutil
from game_info import candies_info

width = shutil.get_terminal_size().columns
position = (width - max(map(len, candies_info))) // 2

for info in candies_info:
    print(info.center(width))

player1 = input('Введите имя первого любителя сладкого: ')
player2 = input('Введите имя второго любителя сладкого: ')
candies = int(input('Сколькими конфетками играть будем? '))
candy_move = int(input('Сколько конфет за ход можно брать? '))
print()
print('Окей, летсгоу...', '\n')

turn = 0
while candies > candy_move:
    if turn == 0:
        move = int(input(f'{player1}, сколько возьмёшь конфет? '))
        while 1 > move or candy_move < move:
            print('Мы же условились...возьми столько, сколько договорились.')
            move = int(input('Давай ещё раз. Сколько конфет берёшь? '))
        turn = 1
    else:
        move = int(input(f'{player2}, сколько возьмёшь конфет? '))
        while 1 > move or candy_move < move:
            print('Мы же условились...возьми столько, сколько договорились.')
            move = int(input('Давай ещё раз. Сколько конфет берёшь? '))
        turn = 0
    candies -= move
    print(f'Осталось {candies} конфет.', '\n')
if turn == 0:
    print(f'{player1} одерживает победу. Диабет обеспечен.')
else:
    print(f'{player2} одерживает победу. Диабет обеспечен.')