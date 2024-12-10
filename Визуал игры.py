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
