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


if __name__ == '__main__':
    unittest.main()
