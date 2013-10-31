import unittest
import tictactoe


class CreateGridTests(unittest.TestCase):
    """Tests for the create_grid function."""
    def setUp(self):
        self.grid = tictactoe.create_grid()

    def test_create_grid_returns_list_of_nine_elements(self):
        grid_length = len(self.grid)

        self.assertEqual(grid_length, 9)

    def test_create_grid_returns_list_of_spaces(self):
        expected = " "

        for element in self.grid:
            self.assertEqual(element, expected)


class BinaryQuestionTests(unittest.TestCase):
    """Tests for the ask_binary_question function."""
    def test_ask_binary_question_with_y_returns_true(self):
        result = tictactoe.ask_binary_question(lambda: "y")

        self.assertEqual(result, True)

    def test_ask_binary_question_with_n_returns_false(self):
        result = tictactoe.ask_binary_question(lambda: "n")

        self.assertEqual(result, False)

    def test_ask_binary_question_with_invalid_returns_none(self):
        result = tictactoe.ask_binary_question(lambda: "m")

        self.assertIsNone(result)

    def test_ask_binary_question_with_Y_returns_true(self):
        result = tictactoe.ask_binary_question(lambda: "Y")

        self.assertEqual(result, True)

    def test_ask_binary_question_with_N_returns_true(self):
        result = tictactoe.ask_binary_question(lambda: "N")

        self.assertEqual(result, False)


class NumberQuestionTests(unittest.TestCase):
    """Tests for the ask_number_question function."""
    def test_ask_number_question_with_one_returns_0(self):
        result = tictactoe.ask_number_question(lambda: "1")

        self.assertEqual(result, 0)

    def test_ask_number_question_with_two_returns_2(self):
        result = tictactoe.ask_number_question(lambda: "2")

        self.assertEqual(result, 1)

    def test_ask_number_question_with_invalid_number_returns_none(self):
        result = tictactoe.ask_number_question(lambda: "0")

        self.assertIsNone(result)

    def test_ask_number_question_with_non_number_returns_none(self):
        result = tictactoe.ask_number_question(lambda: "y")

        self.assertIsNone(result)


class PlacePieceTests(unittest.TestCase):
    """Tests for the place function."""
    def setUp(self):
        self.grid = tictactoe.create_grid()

    def test_place_with_one_and_X_sets_cell_one_to_X(self):
        tictactoe.place(self.grid, 1, "X")

        self.assertEqual(self.grid[1], "X")

    def test_place_with_one_and_O_sets_cell_one_to_O(self):
        tictactoe.place(self.grid, 1, "O")

        self.assertEqual(self.grid[1], "O")

    def test_place_with_invalid_piece_raises_value_error(self):
        self.assertRaises(ValueError, tictactoe.place, self.grid, 1, "Y")


class RemovePieceTests(unittest.TestCase):
    """Tests for the remove_piece function."""
    def test_remove_piece_with_one_sets_cell_one_to_space(self):
        grid = tictactoe.create_grid()
        grid[1] = "X"

        tictactoe.remove_piece(grid, 1)

        self.assertEqual(grid[1], " ")


class LegalMovesTests(unittest.TestCase):
    """Tests for the get_legal_moves function."""
    def setUp(self):
        self.grid = tictactoe.create_grid()

    def test_get_legal_moves_when_all_moves_legal_returns_full_list(self):
        legal = tictactoe.get_legal_moves(self.grid)
        legal_length = len(legal)

        self.assertEqual(legal_length, 9)

    def test_get_legal_moves_when_eight_moves_legal_returns_list_of_8(self):
        self.grid[2] = "X"

        legal = tictactoe.get_legal_moves(self.grid)
        legal_length = len(legal)

        self.assertEqual(legal_length, 8)

    def test_get_legal_moves_when_no_moves_legal_returns_empty_list(self):
        for i in range(9):
            self.grid[i] = "X"

        legal = tictactoe.get_legal_moves(self.grid)
        legal_length = len(legal)

        self.assertEqual(legal_length, 0)


class SwitchTurnTests(unittest.TestCase):
    """Tests for the switch function."""
    def test_switch_when_turn_is_true_returns_false(self):
        turn = True

        turn = tictactoe.switch(turn)

        self.assertEqual(turn, False)

    def test_switch_when_turn_is_false_returns_true(self):
        turn = False

        turn = tictactoe.switch(turn)

        self.assertEqual(turn, True)


class WinnerTests(unittest.TestCase):
    """Tests for the get_winner function."""
    def setUp(self):
        self.grid = tictactoe.create_grid()

        self.grid[0] = "X"
        self.grid[1] = "O"
        self.grid[2] = "X"
        self.grid[3] = "X"
        self.grid[4] = "O"
        self.grid[5] = "O"
        self.grid[6] = "O"
        self.grid[7] = "X"
        self.grid[8] = "X"

    def test_get_winner_with_top_row_X_returns_X(self):
        self.grid[0] = "X"
        self.grid[1] = "X"
        self.grid[2] = "X"

        winner = tictactoe.get_winner(self.grid)

        self.assertEqual(winner, "X")

    def test_get_winner_with_top_row_O_returns_O(self):
        self.grid[0] = "O"
        self.grid[1] = "O"
        self.grid[2] = "O"

        winner = tictactoe.get_winner(self.grid)

        self.assertEqual(winner, "O")

    def test_get_winner_with_left_column_X_returns_X(self):
        self.grid[0] = "X"
        self.grid[3] = "X"
        self.grid[6] = "X"

        winner = tictactoe.get_winner(self.grid)

        self.assertEqual(winner, "X")

    def test_get_winner_with_full_grid_and_no_combo_returns_tie(self):
        winner = tictactoe.get_winner(self.grid)

        self.assertEqual(winner, "tie")

    def test_get_winner_with_empty_cells_returns_none(self):
        grid = tictactoe.create_grid()

        winner = tictactoe.get_winner(grid)

        self.assertIsNone(winner)


if __name__ == '__main__':
    unittest.main()
