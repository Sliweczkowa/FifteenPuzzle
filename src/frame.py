import copy
from typing import List


dictionary = {
    (-1, 0): 'D',
    (1, 0): 'U',
    (0, -1): 'R',
    (0, 1): 'L'
}


class Frame:

    def __init__(self, r: int, c: int, vals: List[int], moved='', cost=0, board_cost=0):
        self.row_count = self.set_row_count(r)
        self.column_count = self.set_column_count(c)
        self.game_board = self.validate_game_board(vals)
        self.winning_board = [i for i in range(1, r * c)] + [0]
        self.moved = moved
        self.cost = cost
        self.board_cost = 0

    def __eq__(self, other):
        return (self.row_count == other.row_count and
                self.column_count == other.column_count and
                self.game_board == other.game_board)

    def set_column_count(self, row) -> int:
        if type(row) is not int:
            raise Exception("row must be of type int")
        if row < 2:
            raise Exception("row must be greater or equal 2")
        return row

    def set_row_count(self, col) -> int:
        if type(col) is not int:
            raise Exception("column must be of type int")
        if col < 2:
            raise Exception("column must be greater or equal 2")
        return col

    def validate_game_board(self, new_board) -> List[int]:
        if len(new_board) is not self.row_count * self.column_count:
            raise Exception("values len must be the product of row and column")
        if not all(type(v) is int for v in new_board):
            raise Exception("all values items must be of type int")
        if not all(-1 < v < self.row_count * self.column_count for v in new_board):
            raise Exception("all values items must be of value (-1, row*column)")
        if len(new_board) is not len(set(new_board)):
            raise Exception("values items must not repeat")
        return new_board

    def validate_win(self) -> bool:
        return self.winning_board == self.game_board

    def get_blank_pos(self) -> tuple[int, int]:
        blank_index = self.game_board.index(0)
        return divmod(blank_index, self.column_count)

    def get_blank_index(self) -> int:
        return self.game_board.index(0)

    def get_legal_moves(self, blank_row, blank_col) -> set[tuple[int, int]]:

        legal_moves = set()

        if blank_row > 0:
            legal_moves.add((-1, 0))  # Piece having freedom moved down - D
        if blank_row < self.row_count - 1:
            legal_moves.add((1, 0))  # Piece having freedom moved up - U
        if blank_col > 0:
            legal_moves.add((0, -1))  # Piece having freedom moved right - R
        if blank_col < self.column_count - 1:
            legal_moves.add((0, 1))  # Piece having freedom moved left - L

        return legal_moves

    def get_legal_positions_tuple(self, blank_row, blank_col) -> set[tuple[int, int]]:

        legal_moves = set()

        if blank_row > 0:
            legal_moves.add((blank_row - 1, blank_col))  # Piece having freedom moved down - D
        if blank_row < self.row_count - 1:
            legal_moves.add((blank_row + 1, blank_col))  # Piece having freedom moved up - U
        if blank_col > 0:
            legal_moves.add((blank_row, blank_col - 1))  # Piece having freedom moved right - R
        if blank_col < self.column_count - 1:
            legal_moves.add((blank_row, blank_col + 1))  # Piece having freedom moved left - L

        return legal_moves

    def get_legal_positions_dict(self, blank_row, blank_col) -> dict[str, tuple[int, int]]:

        legal_moves = {}

        if blank_row > 0:
            legal_moves['U'] = (blank_row - 1, blank_col)  # Piece having freedom moved down - D
        if blank_row < self.row_count - 1:
            legal_moves['D'] = (blank_row + 1, blank_col)  # Piece having freedom moved up - U
        if blank_col > 0:
            legal_moves['L'] = (blank_row, blank_col - 1)  # Piece having freedom moved right - R
        if blank_col < self.column_count - 1:
            legal_moves['R'] = (blank_row, blank_col + 1)  # Piece having freedom moved left - L

        return legal_moves

    def move(self, legal_moves: set[int], direction, blank_pos: int) -> None:
        if direction in legal_moves:
            self.game_board[blank_pos], self.game_board[blank_pos + direction[0] * self.row_count + direction[1]] = \
                self.game_board[
                    blank_pos + direction[0] * self.row_count + direction[1]], self.game_board[blank_pos]

    def get_moved_boards(self) -> dict[str, List[int]]:
        blank_pos = self.get_blank_pos()
        legal_moves = self.get_legal_positions_dict(blank_pos[0], blank_pos[1])
        moved_boards = {}

        for key, move in legal_moves.items():
            new_board = self.game_board[:]
            blank_index = self.get_blank_index()
            move_index = translate_2d_to_int(move, self.column_count)
            new_board[blank_index], new_board[move_index] = new_board[move_index], new_board[blank_index]
            moved_boards[key] = new_board

        return moved_boards


def translate_legal_moves_to_chr(tuple_moves: set[tuple[int, int]]) -> set[chr]:
    return set(dictionary.get(m) for m in tuple_moves)


def translate_2d_to_int(tuple_coords: tuple[int, int], columns_no: int) -> int:
    return tuple_coords[0] * columns_no + tuple_coords[1]


def moved_frame(frame: Frame, blank_pos: int, not_blank_pos: int) -> Frame:
    moved_board = copy.deepcopy(frame.game_board)
    moved_board[blank_pos] = frame.game_board[not_blank_pos]
    moved_board[not_blank_pos] = 0
    return Frame(frame.row_count, frame.column_count, moved_board)


def create_frame_from_file(file_path: str) -> Frame:
    with open(file_path, 'r') as file:
        first_line = file.readline().strip()
        R, C = map(int, first_line.split())

        data = [[int(v) for v in i.strip().split(' ')] for i in file.readlines()]
        flattened = [item for sublist in data for item in sublist]

    return Frame(R, C, flattened)


def get_board_for_solved(frame, inp):
    boards = [frame.game_board]
    for move in inp:
        moved_board = frame.get_moved_boards()[move]
        frame = Frame(frame.row_count, frame.column_count, moved_board, frame.moved)
        boards.append(frame.game_board)

    return boards


def save_boards_to_file(frame, inp, filename):
    boards = get_board_for_solved(frame, inp)

    with open(filename, 'w') as f:
        f.write(f"{frame.row_count} {frame.column_count}\n")
        for board in boards:
            f.write(' '.join(map(str, board)) + '\n')
