# Функция для проверки ничьей
def check_draw(board):
    return all([cell != " " for row in board for cell in row])
# Функция для обработки хода игрока
def player_move(row, col):
    global current_player
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