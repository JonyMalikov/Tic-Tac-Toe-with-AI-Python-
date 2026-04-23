def print_board(board):
    print("---------")
    for i in range(0, 9, 3):
        row = board[i : i + 3]
        print(f"| {row[0]} {row[1]} {row[2]} |")
    print("---------")


initial_board = [" "] * 9
print("Пустое поле:")
print_board(initial_board)

test_board = ["X", "O", " ", " ", "X", " ", "O", " ", " "]
print("\nПоле с текстовыми данными:")
print_board(test_board)
