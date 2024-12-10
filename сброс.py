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