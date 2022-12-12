import shutil
from game_info import candies_info

width = shutil.get_terminal_size().columns
position = (width - max(map(len, candies_info))) // 2

for info in candies_info:
    print(info.center(width))

player = input('Как тебя зовут, сладкоежка? ')
candies = int(input('Сколькими конфетками играть будем? '))
candy_move = int(input('Сколько конфет за ход можно брать? '))
print()
print('Окей, летсгоу...', '\n')

turn = 0
while candies > candy_move:
    if turn == 0:
        move = int(input(f'{player}, сколько возьмёшь конфет? '))
        while 1 > move or candy_move < move:
            print('Мы же условились...возьми столько, сколько договорились.')
            move = int(input('Давай ещё раз. Сколько конфет берёшь? '))
        turn = 1
    else:
        move = candies % (candy_move + 1)
        if move == 0:
            move = candies % candy_move # иначе компьютер будет брать 0 конфет, если пользователь будет играть по выигрышной стратегии, что плохо
        turn = 0
        print(f'Компьютер берёт {move} конфет.')
    candies -= move
    print(f'Осталось {candies} конфет.', '\n')
if turn == 0:
    print(f'{player} одерживает победу. Диабет обеспечен.')
else:
    print(f'Компьютер одерживает победу над кожаным.')