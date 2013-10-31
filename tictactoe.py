GRID_SIZE = 9
SPACE = " "


def create_grid():
    """Creates a tic tac toe grid."""
    return [SPACE for cell in range(GRID_SIZE)]


def ask_binary_question(get_binary_response):
    """Returns True if "y", False if "n", otherwise returns None."""
    if get_binary_response().lower() == "y":
        return True

    if get_binary_response().lower() == "n":
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

    return None


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


def get_winner(grid):
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
            return grid[state[0]]

    if SPACE not in grid:
        return "tie"

    return None
