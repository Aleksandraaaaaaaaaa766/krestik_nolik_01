# krestik_nolik_011
import tkinter as tk
from tkinter import messagebox

# Функция для проверки  победы
def check_win(board, player):
    # Проверка горизонталей
    for row in board:
        if all([cell == player for cell in row]):
            return True
    # Проверка вертикалей
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    # Проверка диагоналей
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False


# Функция для проверки ничьей
def check_draw(board):
    return all([cell != " " for row in board for cell in row])
    
# Функция для обработки хода игрока
def player_move(row, col):
     current_player
    if board[row][col] == " ":
        board[row][col] = current_player
        buttons[row][col].config(text=current_player, state="disabled")
        
        # Проверка на победу
        if check_win(board, current_player):
            messagebox.showinfo("Победа!", f"Игрок {current_player} победил!")
            reset_game()
        # Проверка на ничью
        elif check_draw(board):
            messagebox.showinfo("Ничья!", "Ничья!")
            reset_game()
        else:
            # Смена игрока
            # В переменную записывается О, если был Х, иначе Х
            current_player = "O" if current_player == "X" else "X"


# Функция для сброса игры
def reset_game():
    global board, current_player
    # Сбросим игровое поле
    board = [[" " for _ in range(3)] for _ in range(3)]
    # Обновим кнопки
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text=" ", state="normal")
    current_player = "X"  # Начинает всегда игрок X


# Создание окна
root = tk.Tk()
root.title("Крестики-Нолики")
# Инициализация глобальных переменных

# создаётся поле 3*3 из пустых строк. работаем с матрицей
board = [[" " for _ in range(3)] for _ in range(3)]
current_player = "X"  # Игрок X начинает первым

# Создание кнопок для игрового поля
buttons = [[None for _ in range(3)] for _ in range(3)]
for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text=" ", font=('normal', 40), width=5, height=2,
                                  command=lambda row=i, col=j: player_move(row, col))
        buttons[i][j].grid(row=i, column=j)
        
# Кнопка для сброса игры
reset_button = tk.Button(root, text="Сбросить игру", font=('normal', 14), command=reset_game)
reset_button.grid(row=3, column=0, columnspan=3)

# Запуск игры
root.mainloop()
