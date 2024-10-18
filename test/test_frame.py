import unittest

from src.frame import Frame


class TestFrame(unittest.TestCase):

    def test_frame_dimensions(self):
        # Parameters row and column must be of type int
        self.assertRaises(Exception, Frame, 4.15, 4, [])
        self.assertRaises(Exception, Frame, 4, 5.99, [])
        # Parameters row and column must be grater than 0
        # self.assertRaises(Exception, Frame, 4, 0, [])  # TODO: frame.py
        # self.assertRaises(Exception, Frame, 0, 4, [])  # TODO: frame.py

    def test_frame_values(self):
        # Parameter values' length must be the product of row and column
        self.assertRaises(Exception, Frame, 4, 4, [v for v in range(0, 4)])
        # All items of parameter values must be of type int
        self.assertRaises(Exception, Frame, 4, 4, [v/10 for v in range(0, 16)])
        # All values' items must be of value <0, row*column)
        self.assertRaises(Exception, Frame, 4, 4, [v-1 for v in range(0, 16)])
        self.assertRaises(Exception, Frame, 4, 4, [v+1 for v in range(0, 16)])
        # Parameter values' items values must not repeat
        self.assertRaises(Exception, Frame, 4, 4, [v for v in range(0, 14)] + [14, 14])


if __name__ == '__main__':
    unittest.main()
