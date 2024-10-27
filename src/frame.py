from typing import List


class Frame:

    def __init__(self, r: int, c: int, vals: List[int]):
        self.row_count = self.set_row_count(r)
        self.column_count = self.set_column_count(c)
        self.game_board = self.validate_game_board(vals)
        self.winning_board = [i for i in range(r * c)]

    def set_column_count(self, row):
        if type(row) is not int:
            raise Exception("row must be of type int")
        return row

    def set_row_count(self, col):
        if type(col) is not int:
            raise Exception("column must be of type int")
        # TODO: add exception for minimal value
        return col

    def validate_game_board(self, new_board) -> List[int]:
        if len(new_board) is not self.row_count * self.column_count:
            raise Exception("values len must be the product of row and column")
        if not all(type(v) is int for v in new_board):
            raise Exception("all values items must be of type int")
        if not all(-1 < v < self.row_count * self.column_count for v in new_board):
            raise Exception("all values items must be of value <-1, row*column)")
        if len(new_board) is not len(set(new_board)):
            raise Exception("values items must not repeat")
        return new_board

    def validate_win(self) -> bool:
        return self.winning_board == self.game_board

    def get_blank_pos(self) -> tuple[int]:
        blank_index = self.game_board.index(0)
        return divmod(blank_index, self.column_count)

    def get_legal_moves(self, blank_row, blank_col) -> set[tuple[int,int]]:

        legal_moves = set()

        if blank_row > 0:
            legal_moves.add((-1, 0))
        if blank_row < self.row_count - 1:
            legal_moves.add((1, 0))
        if blank_col > 0:
            legal_moves.add((0, -1))
        if blank_col < self.column_count - 1:
            legal_moves.add((0, 1))

        return legal_moves

    def move(self, legal_moves: set[int], direction, blank_pos: int):
        if direction in legal_moves:
            self.game_board[blank_pos], self.game_board[blank_pos + direction[0] * self.row_count + direction[1]] = \
                self.game_board[
                    blank_pos + direction[0] * self.row_count + direction[1]], self.game_board[blank_pos]
