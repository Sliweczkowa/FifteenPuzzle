from typing import List


class Frame:

    def __init__(self, r: int, c: int, vals: List[int]):
        self.row_count = self.set_row_count(r)
        self.column_count = self.set_column_count(r)
        self.game_board = self.validate_game_board(vals)
        self.winning_board = [i for i in range(r * c)]

    def set_column_count(self, row):
        if type(row) is not int:
            raise Exception("row must be of type int")
        self.row_count = row

    def set_row_count(self, col):
        if type(col) is not int:
            raise Exception("column must be of type int")
        # TODO: add exception for minimal value
        self.column_count = col

    def validate_game_board(self, new_board):
        if len(new_board) is not self.row_count * self.column_count:
            raise Exception("values len must be the product of row and column")
        if not all(type(v) is int for v in new_board):
            raise Exception("all values items must be of type int")
        if not all(-1 < v < self.row_count * self.column_count for v in new_board):
            raise Exception("all values items must be of value <-1, row*column)")
        if len(new_board) is not len(set(new_board)):
            raise Exception("values items must not repeat")
        self.game_board = new_board

    def validate_win(self) -> bool:
        return self.winning_board == self.game_board
