from collections import deque
from random import shuffle

from src.frame import Frame


def dfs(frame: Frame, order_of_moves):
    already_moved = set()

    if order_of_moves[0] == 'R':
        random_order = True
    else:
        random_order = False

    queue = deque([frame])
    while True:
        current_frame = queue.popleft()
        moved_frames = current_frame.get_moved_boards()
        if current_frame.validate_win():
            return list(current_frame.moved)

        if random_order:
            shuffle(order_of_moves)
        for direction in reversed(order_of_moves):
            if direction not in moved_frames:
                continue
            new_frame = moved_frames[direction]
            if tuple(new_frame) in already_moved:
                continue
            additive = current_frame.moved + direction
            queue.appendleft(Frame(frame.row_count, frame.column_count, new_frame, additive))
            already_moved.add(tuple(new_frame))
