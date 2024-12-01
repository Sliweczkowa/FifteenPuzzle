from collections import deque
from random import shuffle

from src.frame import Frame


def bfs2(frame: Frame, order_of_moves: list[chr]) -> list[chr]:
    already_moved = set()
    queue = deque([frame])

    row_no = frame.row_count
    column_no = frame.column_count

    if order_of_moves[0] == 'R':
        random_order = True
    else:
        random_order = False

    while True:
        current_frame = queue.popleft()
        moved_frames = current_frame.get_moved_boards()

        if current_frame.validate_win():
            return list(current_frame.moved)

        if random_order:
            shuffle(order_of_moves)
        for direction in order_of_moves:
            if direction not in moved_frames:
                continue
            new_frame = moved_frames[direction]
            if tuple(new_frame) in already_moved:
                continue
            additive = current_frame.moved + direction
            queue.append(Frame(r=row_no, c=column_no, vals=new_frame, moved=additive))
            already_moved.add(tuple(new_frame))
