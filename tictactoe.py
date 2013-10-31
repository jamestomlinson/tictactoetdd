GRID_SIZE = 9
SPACE = " "


def create_grid():
    """Creates a tic tac toe grid."""
    return [SPACE for cell in range(GRID_SIZE)]


def ask_binary_question(get_binary_response):
    """Returns True if "y", False if "n", otherwise returns None."""
    response = get_binary_response().lower()

    if response == "y":
        return True

    elif response == "n":
        return False

    return None


def get_binary_response():
    """Asks the user to enter 'y' or 'n' and returns the input."""
    return raw_input("Enter 'y' or 'n': ")


def ask_number_question(get_number_response):
    """Returns int if number is between 1 and 9, otherwise returns None."""
    try:
        number = int(get_number_response()) - 1

    except:
        return None

    if number in range(GRID_SIZE):
        return number


def get_number_response():
    """Asks the user to enter a number and returns the input."""
    return raw_input("Enter a number: ")


def place(grid, cell, piece):
    """Places piece (X or O) at grid[cell]."""
    if piece in ("X", "O"):
        grid[cell] = piece

    else:
        raise ValueError("Piece must be 'X' or 'O'.")


def remove_piece(grid, cell):
    """Removes piece at grid[cell] by setting it to SPACE."""
    grid[cell] = SPACE


def get_legal_moves(grid):
    """Returns a list of legal moves in the grid."""
    return [move for move in range(GRID_SIZE) if grid[move] == SPACE]


def switch(turn):
    """Switches whether it's the computer's turn or not."""
    return not turn


def get_winner(grid, computer):
    """Determines if there is a winning combination of pieces in grid."""
    win_states = [(0, 1, 2),    # Top row
                  (3, 4, 5),    # Middle row
                  (6, 7, 8),    # Bottom row
                  (0, 3, 6),    # Left column
                  (1, 4, 7),    # Middle column
                  (2, 5, 8),    # Right column
                  (0, 4, 8),    # Negative diagonal
                  (2, 4, 6)]    # Positive diagonal

    for state in win_states:
        if grid[state[0]] == grid[state[1]] == grid[state[2]] != SPACE:
            if grid[state[0]] == computer:
                return 1
            else:
                return -1

    if SPACE not in grid:
        return 0


def print_welcome():
    """Prints the start of game message."""
    print "\nWelcome to Tic Tac Toe!\n"
    print "The game is played on a 3x3 board with the following layout:"
    print """
                1 | 2 | 3
                ---------
                4 | 5 | 6
                ---------
                7 | 8 | 9\n"""
    print "When prompted, select the number that corresponds to your move.\n"
    print "Would you like to go first?"


def get_first_turn():
    """Returns True if the computer goes first, otherwise False."""
    turn = None

    while turn is None:
        turn = ask_binary_question(get_binary_response)

        if turn is None:
            print "Invalid choice. Please try again."

    return not turn


def set_pieces(turn):
    """If the computer goes first, return 'X', 'O', otherwise the opposite."""
    if turn:
        return "X", "O"

    else:
        return "O", "X"


def print_grid(grid):
    """Prints the grid to the console."""
    print
    print "\t", grid[0], "|", grid[1], "|", grid[2]
    print "\t---------"
    print "\t", grid[3], "|", grid[4], "|", grid[5]
    print "\t---------"
    print "\t", grid[6], "|", grid[7], "|", grid[8]
    print


def get_computer_move(grid, computer_turn, computer, player):
    """Returns the computer's move."""
    move, score = find_best_move(grid, computer_turn, computer, player, -1, 1)

    print "Computer chooses " + computer + " at position "\
        + str(move + 1) + ". Your turn."

    return move


def find_best_move(grid, computer_turn, computer, player, alpha, beta):
    """Finds the best move using the minimax algorithm."""
    best_move = None
    best_score = None

    winner = get_winner(grid, computer)

    if winner is not None:
        return best_move, winner

    if computer_turn:
        best_score = alpha
        piece = computer

    else:
        best_score = beta
        piece = player

    for move in get_legal_moves(grid):
        place(grid, move, piece)
        reply_move, reply_score = find_best_move(
                grid, not computer_turn, computer, player, alpha, beta
                )
        remove_piece(grid, move)

        if computer_turn and reply_score > best_score:
            best_move = move
            best_score = reply_score
            alpha = reply_score

        elif not computer_turn and reply_score < best_score:
            best_move = move
            best_score = reply_score
            beta = reply_score

        if alpha >= beta:
            return best_move, best_score

    return best_move, best_score


def get_player_move(grid, player):
    """Returns the player's move choice."""
    print "Select your move by entering a number corresponding to the grid."

    legal_moves = get_legal_moves(grid)
    move = None

    while move not in legal_moves:
        move = ask_number_question(get_number_response)

        if move is None:
            print "Invalid move. Please select a number between 1 and 9."

        elif move not in legal_moves:
            print "Invalid move. That move has already been taken."

    print "Placing " + player + " at position " + str(move + 1) + "."

    return move


def main():
    """Main game loop."""
    print_welcome()

    computer_turn = get_first_turn()
    computer, player = set_pieces(computer_turn)

    grid = create_grid()
    winner = get_winner(grid, computer)

    while winner is None:
        if computer_turn:
            move = get_computer_move(grid, computer_turn, computer, player)
            place(grid, move, computer)

        else:
            move = get_player_move(grid, player)
            place(grid, move, player)

        computer_turn = switch(computer_turn)
        print_grid(grid)
        winner = get_winner(grid, computer)
