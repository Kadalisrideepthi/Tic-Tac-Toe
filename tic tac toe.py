board = [' ' for _ in range(9)]

def show_positions():
    print("\nPositions:")
    print("1 | 2 | 3")
    print("--+---+--")
    print("4 | 5 | 6")
    print("--+---+--")
    print("7 | 8 | 9\n")

def print_board():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()

def check_winner(player):
    if board[0] == board[1] == board[2] == player:
        return True
    if board[3] == board[4] == board[5] == player:
        return True
    if board[6] == board[7] == board[8] == player:
        return True
    if board[0] == board[3] == board[6] == player:
        return True
    if board[1] == board[4] == board[7] == player:
        return True
    if board[2] == board[5] == board[8] == player:
        return True
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True
    return False

def is_draw():
    return ' ' not in board

def player_move(player):
    while True:
        move = input(f"Player {player}, enter position (1-9): ")
        if not move.isdigit():
            print("❌ Please enter a number.")
            continue

        move = int(move)
        if move < 1 or move > 9:
            print("❌ Position must be between 1 and 9.")
        elif board[move - 1] != ' ':
            print("❌ Position already taken.")
        else:
            board[move - 1] = player
            break

def play_game():
    current_player = 'X'
    show_positions()

    while True:
        print_board()
        player_move(current_player)

        if check_winner(current_player):
            print_board()
            print(f"🎉 Player {current_player} wins!")
            break

        if is_draw():
            print_board()
            print("🤝 Game Draw!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

play_game()