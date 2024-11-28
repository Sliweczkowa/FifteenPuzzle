import unittest

from src.frame import Frame
from src.algorithms.bfs import bfs


class TestBFS(unittest.TestCase):

    def test_bfs_8puzzle_1move(self):
        frame = Frame(3, 3, [1, 2, 3, 4, 5, 6, 7, 0, 8])
        self.assertEqual(bfs(frame, 'order'), [(2, 1), (2, 2)])

    def test_bfs_8puzzle_7moves(self):
        frame = Frame(3, 3, [1, 3, 6, 5, 2, 0, 4, 7, 8])
        self.assertEqual(
            bfs(frame, 'order'),
            [(1, 2), (0, 2), (0, 1), (1, 1), (1, 0), (2, 0), (2, 1), (2, 2)]
        )

    def test_bfs_8puzzle_9moves(self):
        frame = Frame(3, 3, [1, 8, 2, 0, 4, 3, 7, 6, 5])
        self.assertEqual(
            bfs(frame, 'order'),
            [(1, 0), (1, 1), (0, 1), (0, 2), (1, 2), (2, 2), (2, 1), (1, 1), (1, 2), (2, 2)]
        )

    def test_bfs_8puzzle_13moves(self):
        frame = Frame(3, 3, [1, 2, 3, 5, 6, 0, 7, 8, 4])
        self.assertEqual(
            bfs(frame, 'order'),
            [(1, 2), (1, 1), (1, 0), (2, 0), (2, 1), (2, 2), (1, 2), (1, 1), (2, 1), (2, 0), (1, 0), (1, 1), (1, 2), (2, 2)]
        )


if __name__ == '__main__':
    unittest.main()
