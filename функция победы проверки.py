# Функция для проверки победы
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
