import unittest

from src.frame import Frame


class TestFrame(unittest.TestCase):

    def test_frame_dimensions(self):
        # Parameters row and column must be of type int
        self.assertRaises(Exception, Frame, 4.15, 4, [])
        self.assertRaises(Exception, Frame, 4, 5.99, [])
        # Parameters row and column must be grater than 0
        self.assertRaises(Exception, Frame, 4, 2, [])
        self.assertRaises(Exception, Frame, 0, 4, [])

    def test_frame_values(self):
        # Parameter values' length must be the product of row and column
        self.assertRaises(Exception, Frame, 4, 4, [v for v in range(0, 4)])
        # All items of parameter values must be of type int
        self.assertRaises(Exception, Frame, 4, 4, [v / 10 for v in range(0, 16)])
        # All values' items must be of value <0, row*column)
        self.assertRaises(Exception, Frame, 4, 4, [v - 1 for v in range(0, 16)])
        self.assertRaises(Exception, Frame, 4, 4, [v + 1 for v in range(0, 16)])
        # Parameter values' items values must not repeat
        self.assertRaises(Exception, Frame, 4, 4, [v for v in range(0, 14)] + [14, 14])

    def test_if_correct_frame_wins(self):
        f = Frame(2, 2, [0, 1, 2, 3])

        self.assertTrue(f.validate_win())

    def test_get_blank_pos(self):
        # Initialize Frame with known values
        frame = Frame(3, 3, [1, 2, 3, 4, 0, 5, 6, 7, 8])

        # Call get_blank_pos and assert the expected result
        self.assertEqual(frame.get_blank_pos(), (1, 1))

    def test_get_legal_moves(self):
        # Initialize Frame with known values
        frame = Frame(3, 3, [1, 2, 3, 4, 0, 5, 6, 7, 8])

        # Test legal moves for blank position (1, 1)
        self.assertEqual(frame.get_legal_moves(1, 1), {(-1, 0), (1, 0), (0, -1), (0, 1)})

        # Test legal moves for blank position (0, 0)
        frame.game_board = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.assertEqual(frame.get_legal_moves(0, 0), {(1, 0), (0, 1)})

        # Test legal moves for blank position (2, 2)
        frame.game_board = [1, 2, 3, 4, 5, 6, 7, 8, 0]
        self.assertEqual(frame.get_legal_moves(2, 2), {(-1, 0), (0, -1)})



if __name__ == '__main__':
    unittest.main()

