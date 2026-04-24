def print_board(board):
    """
    Выводит игровое поле 3x3 в читаемом формате.
    board: список из 9 символов, например ['X', 'O', ' ', ...]
    """
    print("---------")
    for i in range(0, 9, 3):
        row = board[i : i + 3]
        print(f"| {row[0]} {row[1]} {row[2]} |")
    print("---------")


def player_move(board):
    """
    Запрашивает ход игрока, проверяет корректность ввода
    и возвращает индекс выбранной клетки (0–8).
    """
    while True:
        try:
            coords = input("Введите координаты (строка столбец): ").split()
            if len(coords) != 2:
                print("Ошибка: введите два числа через пробел.")
                continue

            row, col = int(coords[0]), int(coords[1])

            # Проверка диапазона 1–3
            if not (1 <= row <= 3 and 1 <= col <= 3):
                print("Ошибка: координаты должны быть от 1 до 3.")
                continue

            # Преобразование в индекс одномерного массива (0–8)
            index = (row - 1) * 3 + (col - 1)

            # Проверка, свободна ли клетка
            if board[index] != " ":
                print("Ошибка: эта клетка уже занята.")
                continue

            return index

        except ValueError:
            print("Ошибка: введите целые числа.")


# --- Основной код для проверки Шага 2 ---
if __name__ == "__main__":
    # Создаём пустое поле (список из 9 пробелов)
    board = [" "] * 9
    print("Начальное поле:")
    print_board(board)

    # Имитируем один ход игрока
    print("\nХод игрока X:")
    move_index = player_move(board)
    board[move_index] = "X"

    print("\nПоле после хода:")
    print_board(board)
