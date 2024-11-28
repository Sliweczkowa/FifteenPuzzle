from src.frame import *


# TODO: sort moves by 'order' parameter and output to ordered array
def bfs(board: Frame, order: list[chr]) -> list[chr] | int:

    # Get blank info
    (blank_row, blank_col) = board.get_blank_pos()
    blank_position_tuple = (blank_row, blank_col)
    blank_position_int = translate_2d_to_int(blank_position_tuple, board.column_count)

    # Mark blank position as visited
    visited_positions = [blank_position_tuple]

    # Get possible frames
    legal_positions = board.get_legal_positions_tuple(blank_row, blank_col)  # unordered set of tuples
    legal_frames = [(moved_frame(board, blank_position_int, translate_2d_to_int(x, board.column_count)), visited_positions + [x])
                    for x in legal_positions]

    for frame, visited in legal_frames:

        # Check for win
        if frame.validate_win() is True:
            return visited

        # If not won add more
        else:
            legal_positions = frame.get_legal_positions_tuple(*frame.get_blank_pos())  # unordered set of tuples
            frame_blank_position_int = translate_2d_to_int(frame.get_blank_pos(), frame.column_count)
            legal_frames_to_check = [
                (moved_frame(frame, frame_blank_position_int, translate_2d_to_int(x, frame.column_count)),
                 visited + [x]) for x in legal_positions]
            for to_check, v1 in legal_frames_to_check:
                in_array = False
                for not_repeated, v2 in legal_frames:
                    if to_check.__eq__(not_repeated):
                        in_array = True
                if not in_array:
                    legal_frames.append((to_check, v1))

    return -1


# f = bfs(Frame(3, 3, [1, 2, 3, 5, 6, 0, 7, 8, 4]), 1)
# b = bfs(Frame(3, 3, [1, 0, 2, 3, 4, 5, 6, 7, 8]), 1)
e = bfs(Frame(3, 3, [1, 2, 3, 4, 5, 6, 7, 0, 8]), 1)
# a = bfs(Frame(3, 3, [5, 4, 8, 6, 0, 1, 7, 2, 3]), 1)
# c = bfs(Frame(4, 4, [13, 2, 10, 3, 1, 12, 8, 4, 5, 0, 9, 6, 15, 14, 11, 7]), 1)
# d = bfs(Frame(3, 3, [1, 8, 2, 0, 4, 3, 7, 6, 5]), 1)

# print(d)

i = 0
