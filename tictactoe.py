GRID_SIZE = 9
SPACE = " "


def create_grid():
    """Creates a tic tac toe grid."""
    return [SPACE for cell in range(GRID_SIZE)]


def ask_binary_question(get_binary_response):
    """Returns True if "y", False if "n", otherwise keeps asking."""
    if get_binary_response().lower() == "y":
        return True

    if get_binary_response().lower() == "n":
        return False

    return None


def get_binary_response():
    """Asks the user to enter 'y' or 'n' and returns the input."""
    return raw_input("Enter 'y' or 'n': ")


def ask_number_question(get_number_response):
    """Returns int if number is between 1 and 9, otherwise keeps asking."""
    try:
        number = int(get_number_response())

    except:
        return None

    if number in range(1, GRID_SIZE + 1):
        return number - 1

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
