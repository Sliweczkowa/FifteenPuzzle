from collections import deque

from src.frame import Frame

already_moved = set()


def bfs2(frame: Frame, order_of_moves: list[str]):
    queue = deque([frame])
    while True:
        current_frame = queue.popleft()
        moved_frames = current_frame.get_moved_boards()
        if current_frame.game_board == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]:
            print('found')
            print(current_frame.moved)
            print(len(current_frame.moved))
            print(len(already_moved))
            exit()

        for direction in order_of_moves:
            if direction not in moved_frames:
                continue
            new_frame = moved_frames[direction]
            if tuple(new_frame) in already_moved:
                continue
            # if not is_solvable(new_frame):
            #     continue
            additive = current_frame.moved + direction
            queue.append(Frame(4, 4, new_frame, additive))
            already_moved.add(tuple(new_frame))



frame1 = Frame(4, 4,
              [1,7,2,3
                   ,5,0,11,4,
                    9,6,12,8
                   ,13,10,14,15]
              )
direct = ['R', 'L', 'D', 'U']


bfs2(frame1, direct)

