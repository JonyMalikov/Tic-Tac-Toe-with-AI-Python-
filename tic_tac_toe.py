import random
import time

# --- Вспомогательные функции ---


def print_board(board):
    """Выводит игровое поле 3x3 в читаемом формате."""
    print("---------")
    for i in range(0, 9, 3):
        row = board[i : i + 3]
        print(f"| {row[0]} {row[1]} {row[2]} |")
    print("---------")


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


def check_game_over(board, vs_ai=False):
    """Проверяет окончание игры. Возвращает True, если игра окончена."""
    if check_winner(board, "X"):
        if vs_ai:
            print("\n🏆 Вы победили! Поздравляем!")
        else:
            print("\n🏆 Победа! Игрок X выиграл!")
        return True
    if check_winner(board, "O"):
        if vs_ai:
            print("\n🤖 Компьютер победил!")
        else:
            print("\n🏆 Победа! Игрок O выиграл!")
        return True
    if is_board_full(board):
        print("\n🤝 Ничья! Поле заполнено.")
        return True
    return False


# --- Ходы игроков ---


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


# --- ИИ: случайные ходы ---


def ai_random_move(board):
    """Возвращает индекс случайной свободной клетки."""
    free_cells = [i for i, cell in enumerate(board) if cell == " "]
    return random.choice(free_cells)


# --- ИИ: Минимакс ---


def minimax(board, is_maximizing):
    """
    Алгоритм Минимакс.
    is_maximizing=True  — ход ИИ (O), ищем максимум.
    is_maximizing=False — ход человека (X), ищем минимум.
    """
    if check_winner(board, "O"):
        return 10
    if check_winner(board, "X"):
        return -10
    if is_board_full(board):
        return 0

    free_cells = [i for i, cell in enumerate(board) if cell == " "]

    if is_maximizing:
        best_score = float("-inf")
        for cell in free_cells:
            board[cell] = "O"
            score = minimax(board, False)
            board[cell] = " "
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = float("inf")
        for cell in free_cells:
            board[cell] = "X"
            score = minimax(board, True)
            board[cell] = " "
            best_score = min(best_score, score)
        return best_score


def ai_minimax_move(board):
    """Выбирает лучший ход для ИИ (O) с помощью Минимакса."""
    best_score = float("-inf")
    best_move = None
    free_cells = [i for i, cell in enumerate(board) if cell == " "]

    for cell in free_cells:
        board[cell] = "O"
        score = minimax(board, False)
        board[cell] = " "
        if score > best_score:
            best_score = score
            best_move = cell

    return best_move


# --- Основной игровой цикл ---


def main():
    board = [" "] * 9
    move_count = 0

    print("Добро пожаловать в Крестики-нолики!")
    print("Игрок X ходит первым.\n")

    # Выбор режима
    print("Выберите режим игры:")
    print("1 — два игрока")
    print("2 — игра против ИИ")
    mode = input("Ваш выбор (1/2): ").strip()
    while mode not in ("1", "2"):
        mode = input("Введите 1 или 2: ").strip()
    vs_ai = mode == "2"

    # Выбор сложности
    ai_difficulty = "easy"
    if vs_ai:
        print("\nВыберите сложность ИИ:")
        print("1 — лёгкий (случайные ходы)")
        print("2 — сложный (непобедимый Минимакс)")
        diff = input("Ваш выбор (1/2): ").strip()
        while diff not in ("1", "2"):
            diff = input("Введите 1 или 2: ").strip()
        ai_difficulty = "easy" if diff == "1" else "hard"

    # Игровой цикл
    while True:
        print_board(board)
        current_player = "X" if move_count % 2 == 0 else "O"
        print(f"Ход игрока {current_player}")

        if vs_ai and current_player == "O":
            print("Компьютер думает...")
            time.sleep(0.5)
            if ai_difficulty == "easy":
                index = ai_random_move(board)
            else:
                index = ai_minimax_move(board)
            print(f"Компьютер выбрал клетку {index // 3 + 1} {index % 3 + 1}")
        else:
            index = player_move(board)

        board[index] = current_player

        if check_game_over(board, vs_ai):
            print_board(board)
            break

        move_count += 1


if __name__ == "__main__":
    main()
