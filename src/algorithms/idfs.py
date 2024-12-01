from src.frame import Frame

already_moved = set()



frame = Frame(4, 4,
              [1,7,2,3
                   ,5,0,11,4,
                    9,6,12,8
                   ,13,10,14,15]
              )
direct = ['R', 'L', 'D', 'U']

not_solvable = []
# U L D R - 35
# R L D U - 2
# U R D L 34
# D R L U
order = ''
depth = 0

def idfs(frame: Frame, depth, depth_limit):

    if depth>depth_limit:
        return False

    already_moved.add(tuple(frame.game_board))
    moved_frames = frame.get_moved_boards()

    if frame.game_board == [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0]:
        print('found')
        print(frame.moved)
        print(len(frame.moved))
        print(len(already_moved))
        exit()

    for direction in direct:
        if direction not in moved_frames:
            continue
        new_frame = moved_frames[direction]
        if tuple(new_frame) in already_moved:
            continue
        additive = frame.moved + direction
        idfs(Frame(4, 4, new_frame, additive ), depth+1, depth_limit)


search_Depth = 1
idfs(frame, depth, 1)

while True:
    r = idfs(frame, depth, search_Depth)
    search_Depth+=1
    already_moved.clear()

    if r:
        break


