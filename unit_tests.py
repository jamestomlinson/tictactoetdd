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


if __name__ == '__main__':
    unittest.main()
