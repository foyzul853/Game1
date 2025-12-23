# Tic-Tac-Toe game by Foyzul Islam Riaz

def print_banner():
    print("*" * 40)
    print("🎮  Welcome to Tic-Tac-Toe  🎮")
    print("        by 𝓕𝓸𝔂𝔷𝓾𝓵 𝓘𝓼𝓵𝓪𝓶 𝓡𝓲𝓪𝔃        ")
    print("*" * 40)
    print()

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all(s == player for s in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0

    for move in range(9):
        print_board(board)
        player = players[turn % 2]
        print(f"Player {player}'s turn")

        while True:
            try:
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter column (0-2): "))
                if board[row][col] == " ":
                    board[row][col] = player
                    break
                else:
                    print("Cell already taken. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Use numbers 0-2.")

        if check_winner(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            return

        turn += 1

    print_board(board)
    print("It's a tie!")

if __name__ == "__main__":
    print_banner()
    tic_tac_toe()
