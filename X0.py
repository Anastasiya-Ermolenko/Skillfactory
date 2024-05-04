board = [1, 2, 3, 4, 5, 6, 7, 8, 9] # игровое поле
def draw_board(): # схема поля на экране
    print("____" * 3 + "_")
    for i in range(3):
        print("|", board[i*3], "|", board[1 + i*3], "|", board[2 + i*3], "|")
        print("____" * 3 + "_")

def motion_player(index, player_value): # ход игрока
    if 1 > index > 9 or board[index - 1] in ("X", "O"):
        return False
    board[index - 1] = player_value
    return True
def check_win(): # победа?
    win = False
    win_combo = ( #выигрышные комбинации
        (0, 1, 2), (3, 4, 5), (6, 7, 8), # горизонтальные
        (0, 3, 6), (1, 4, 7), (2, 5, 8), # вертикальные
        (0, 4, 8), (2, 4, 6)             #диагональ
    )
    for position in win_combo:
      if board[position[0]] == board[position[1]] == board[position[2]]:
          win = board[position[0]]
    return win

def start_game(): # начало игры
    player_value = "X" # игрок X
    motion = 1 # номер хода
    draw_board()
    while motion <= 9 and check_win() == False:
        index = int(input("Ход игрока: " + player_value + ". Введите номер поля: "))
        if (index == 0):
            break
        if motion_player(index, player_value): #ход доступен
            print("Отлично!")
            if player_value == "X":
                player_value = "O" #смена игрока
            else:
                player_value = "X"
            draw_board()
            motion += 1
        else: # ход недоступен
            print("Неверный ход! Повторите!")
    if motion > 9:
        print("Ничья! Игра окончена!")
    else:
        print("Победа за игроком: " + check_win())

print("Добро пожаловать в игру 'Крестики-Нолики'!")
start_game()
