import shutil
from game_info import game_info


def game_field(cell):  # функция чертит игровое поле
    field = (f'\t       |       |       \n'
             f'\t   {cell[1]}   |   {cell[2]}   |   {cell[3]}  \n'
             f'\t_______|_______|_______\n'
             f'\t       |       |       \n'
             f'\t   {cell[4]}   |   {cell[5]}   |   {cell[6]}  \n'
             f'\t_______|_______|_______\n'
             f'\t       |       |       \n'
             f'\t   {cell[7]}   |   {cell[8]}   |   {cell[9]}  \n'
             f'\t       |       |       \n')
    print(field)


def gamers_turn(turn):  # функция меняет ход игроков
    if turn % 2 == 0:
        return 'O'
    else:
        return 'X'


def win_combination(cell):  # функция определяет наличие выигрышной комбинации или отсутствие таковой
    if (cell[1] == cell[2] == cell[3]) \
            or (cell[4] == cell[5] == cell[6]) \
            or (cell[7] == cell[8] == cell[9]):
        return True
    elif (cell[1] == cell[4] == cell[7]) \
            or (cell[2] == cell[5] == cell[8]) \
            or (cell[3] == cell[6] == cell[9]):
        return True
    elif (cell[1] == cell[5] == cell[9]) \
            or (cell[3] == cell[5] == cell[7]):
        return True
    else:
        return False


width = shutil.get_terminal_size().columns
position = (width - max(map(len, game_info))) // 2
for info in game_info:
    print(info.center(width))

print()
player_1 = input('Кто ты, воин? ')
player_2 = input('А твоё имя, воин? ')

cells = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6',
         7: '7', 8: '8', 9: '9'}

gaming = True
end_gaming = False
player_turn = 0
previous_turn = -1

while gaming:
    game_field(cells)
    if previous_turn == player_turn:
        print('Ты, по-моему перепутал...давай ещё разок.')
    previous_turn = player_turn

    if player_turn % 2 == 0:
        print(f'{player_1}, твой ход.')
    else:
        print(f'{player_2}, твой ход.')

    player_move = input('Какую клетку от 1 до 9 займёшь? ')
    if int(player_move) in cells and str.isdigit(player_move):
        if not cells[int(player_move)] in {'X', 'O'}:
            player_turn += 1
            cells[int(player_move)] = gamers_turn(player_turn)
    if win_combination(cells):
        gaming, end_gaming = False, True
    if player_turn > 8:
        gaming = False
if end_gaming:
    if gamers_turn(player_turn) == 'X':
        print(f'{player_1} порвал противника как макака газету!')
    else:
        print(f'{player_2} порвал противника как макака газету!')
else:
    print('Ничья. Давай по-новой.')