def display_game(board):
    print("\n" * 100)
    print(f" {board[1]} | {board[2]} | {board[3]} ")
    print(f"- - - - - -")
    print(f" {board[4]} | {board[5]} | {board[6]} ")
    print(f"- - - - - -")
    print(f" {board[7]} | {board[8]} | {board[9]} ")
    print("\n" * 3)


def select_player():
    player = None
    while player != "X" and player != "O":
        player = input("Player one choose X or O: ").upper()

    if player == "X":
        return ("X", "O")
    else:
        return ("O", "X")


def enter_player_selection(board, player):
    valid_input = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    position = ""
    while position not in valid_input or board[int(position)] != " ":
        position = input(f"Player {player} enter postion: ")
    board[int(position)] = player
    return board


def check_winner(board, player):
    lines = [
        (1, 2, 3),
        (4, 5, 6),
        (7, 8, 9),
        (1, 4, 7),
        (2, 5, 8),
        (3, 6, 9),
        (1, 5, 9),
        (3, 5, 7),
    ]
    for (a, b, c) in lines:
        if board[a] == player and board[b] == player and board[c] == player:
            return player
        else:
            pass
    return None


def check_draw(board):
    if " " in board:
        return False
    else:
        return True


def replay():
    choice = ""
    while choice != "Yes" and choice != "No":
        choice = input("Play again? Enter Yes or No: ")
    if choice == "Yes":
        return True
    else:
        return False


def start_game():
    print("Welcome to Tic Tac Toe")
    print("\n" * 3)

    turn = True
    end_game = False
    board = ["#", " ", " ", " ", " ", " ", " ", " ", " ", " "]

    # select Players
    player1, player2 = select_player()

    # Display display_game
    display_game(board)

    while not end_game:
        # select value
        if(turn):
            # Player one enters pick
            board = enter_player_selection(board, player1)
            # Display board
            display_game(board)
            # check winner
            winner = check_winner(board, player1)
            if winner:
                # end game
                end_game = True
                print(f"*** CONGRATULATIONS player {player1} wins ***")
                print("\n" * 3)
            # check draw
            draw = check_draw(board)
            if draw:
                # end game
                end_game = True
                print("*** DRAW ***")
                print("\n" * 3)
            # switch player
            turn = False
        else:
            # Player Two enters pick
            board = enter_player_selection(board, player2)
            # Display board
            display_game(board)
            # check winner
            winner = check_winner(board, player2)
            if winner:
                # end game
                end_game = True
                print(f"*** CONGRATULATIONS player {player2} wins ***")
                print("\n" * 3)
            # check draw
            draw = check_draw(board)
            if draw:
                # end game
                end_game = True
                print("*** DRAW ***")
                print("\n" * 3)
            # switch player
            turn = True
    # Ask for replay
    is_replay = replay()
    while is_replay:
        # Start game again
        return start_game()

    # THE END
    print("Thanks for playing, Goodbye")
    print("\n" * 3)


start_game()
