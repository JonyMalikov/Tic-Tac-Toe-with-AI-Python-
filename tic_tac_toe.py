import random
import time


def print_board(board):
    """Выводит игровое поле 3x3 в читаемом формате."""
    print("---------")
    for i in range(0, 9, 3):
        row = board[i : i + 3]
        print(f"| {row[0]} {row[1]} {row[2]} |")
    print("---------")


def player_move(board):
    """Запрашивает ход игрока и возвращает индекс клетки (0–8)."""
    while True:
        try:
            coords = input("Введите координаты (строка столбец): ").split()
            if len(coords) != 2:
                print("Ошибка: введите два числа через пробел.")
                continue
            row, col = int(coords[0]), int(coords[1])
            if not (1 <= row <= 3 and 1 <= col <= 3):
                print("Ошибка: координаты должны быть от 1 до 3.")
                continue
            index = (row - 1) * 3 + (col - 1)
            if board[index] != " ":
                print("Ошибка: эта клетка уже занята.")
                continue
            return index
        except ValueError:
            print("Ошибка: введите целые числа.")


def ai_random_move(board):
    """
    Возвращает индекс случайной свободной клетки (0–8).
    """
    free_cells = [i for i, cell in enumerate(board) if cell == " "]
    return random.choice(free_cells)


def check_winner(board, player):
    """Проверяет, выиграл ли заданный игрок."""
    win_combinations = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],  # строки
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],  # столбцы
        [0, 4, 8],
        [2, 4, 6],  # диагонали
    ]
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False


def is_board_full(board):
    """Возвращает True, если нет свободных клеток."""
    return " " not in board


def check_game_over(board):
    """Проверяет окончание игры. Возвращает True, если игра окончена."""
    if check_winner(board, "X"):
        print("\n🏆 Победа! Игрок X выиграл!")
        return True
    if check_winner(board, "O"):
        if vs_ai:  # vs_ai — глобальная? Лучше передать параметром. Исправим ниже.
            print("\n🤖 Компьютер победил!")
        else:
            print("\n🏆 Победа! Игрок O выиграл!")
        return True
    if is_board_full(board):
        print("\n🤝 Ничья! Поле заполнено.")
        return True
    return False


def main():
    """Основной игровой цикл с выбором режима."""
    global vs_ai  # чтобы check_game_over могла использовать
    board = [" "] * 9
    move_count = 0

    print("Добро пожаловать в Крестики-нолики!")
    print("Игрок X ходит первым.\n")

    print("Выберите режим игры:")
    print("1 — два игрока")
    print("2 — игра против ИИ")
    mode = input("Ваш выбор (1/2): ").strip()
    while mode not in ("1", "2"):
        mode = input("Введите 1 или 2: ").strip()
    vs_ai = mode == "2"

    while True:
        print_board(board)
        current_player = "X" if move_count % 2 == 0 else "O"
        print(f"Ход игрока {current_player}")

        if vs_ai and current_player == "O":
            print("Компьютер думает...")
            time.sleep(0.5)
            index = ai_random_move(board)
            print(f"Компьютер выбрал клетку {index // 3 + 1} {index % 3 + 1}")
        else:
            index = player_move(board)

        board[index] = current_player

        if check_game_over(board):
            print_board(board)
            break

        move_count += 1


if __name__ == "__main__":
    main()
