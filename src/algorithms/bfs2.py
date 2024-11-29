from collections import deque

from src.frame import Frame

already_moved = set()


frame = Frame(4, 4,
              [5,1,3,4,0,2,7,8,9,6,10,11,13, 14,15, 12]
              )

# if not is_solvable(frame.game_board):
#     print('unsolvable')
#     exit()

direct = ['R', 'L', 'D', 'U']

not_solvable = []

queue = deque([frame])
order = ''
depth = 0
while True:
    current_frame = queue.popleft()
    moved_frames = current_frame.get_moved_boards()
    if current_frame.game_board == [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0]:
        print('found')
        print(current_frame.moved)
        print(len(current_frame.moved))
        print(len(already_moved))
        exit()

    depth += 1
    for direction in direct:
        if direction not in moved_frames:
            continue
        new_frame = moved_frames[direction]
        if tuple(new_frame) in already_moved:
            continue
        # if not is_solvable(new_frame):
        #     continue
        additive = current_frame.moved + direction
        queue.append(Frame(4, 4, new_frame, additive ))
        already_moved.add(tuple(new_frame))
        t = len(already_moved)
        if t % 13600 == 0:
            print(t / 13600)


# 1 2 3 4
# 5 6 7 8
# 9 10 11 12
# 13 14 15 0

# 1 2 3 4
# 5 6 7 8
# 9 10 11 0
# 13 14 15 12

# 1 2 3 4
# 5 6 7 8
# 9 0 100 11
# 13 14 15 12

# 1 2 3 4
# 5 0 7 8
# 9 6 100 11
# 13 14 15 12

# 1 0 3 4
# 5 2 7 8
# 9 6 100 11
# 13 14 15 12

# 0 1 3 4
# 5 2 7 8
# 9 6 100 11
# 13 14 15 12