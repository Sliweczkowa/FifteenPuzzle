from collections import deque

from src.frame import Frame

already_moved = set()





def dfs(frame: Frame, order_of_moves):
    queue = deque([frame])
    while True:
        current_frame = queue.popleft()
        print(len(already_moved))
        moved_frames = current_frame.get_moved_boards()
        if current_frame.game_board == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]:
            print('found')
            print(current_frame.moved)
            print(len(current_frame.moved))
            print(len(already_moved))
            exit()

        for direction in reversed(order_of_moves):
            if direction not in moved_frames:
                continue
            new_frame = moved_frames[direction]
            if tuple(new_frame) in already_moved:
                continue
            additive = current_frame.moved + direction
            queue.appendleft(Frame(4, 4, new_frame, additive))
            already_moved.add(tuple(new_frame))
            t = len(already_moved)
            if t % 3600 == 0:
                print(t / 3600)



frame = Frame(4, 4,
              [1,2,3,4,5,6,7,8,9,10,11,12,0,13,14,15]
              )
direct = ['R', 'L', 'D', 'U']

dfs(frame, direct)