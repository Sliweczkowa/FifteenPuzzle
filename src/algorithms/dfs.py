from src.frame import *


def dfs(board: Frame,
        zero_coords: tuple[int, int],
        visited_frames: list[Frame],
        order: list[chr]) -> list[chr] | int:

    zero_position = translate_2d_to_int(zero_coords, board.column_count)
    visited_frames.append(board)

    if board.validate_win() is True:
        return [board.get_blank_pos()]

    possible_moves = board.get_legal_moves(zero_coords[0], zero_coords[1])  # unordered set of tuples
    possible_coords = [(m[0] + zero_coords[0], m[1] + zero_coords[1]) for m in possible_moves]

    for pc in possible_coords:
        pc_frame = moved_frame(board, zero_position, translate_2d_to_int(pc, board.column_count))

        if pc_frame not in visited_frames:
            pc_result = dfs(pc_frame, pc, visited_frames, order)
            if pc_result != -1:
                pc_result.append(board.get_blank_pos())
                return pc_result

    return -1


# frame = Frame(3, 3, [5, 4, 8, 6, 0, 1, 7, 2, 3])
frame = Frame(3, 3, [1, 2, 3, 4, 5, 6, 7, 0, 8])
d = dfs(frame, frame.get_blank_pos(), [], 'order')
i = 0
