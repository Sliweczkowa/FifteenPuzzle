from src.frame import Frame

already_moved = set()
362880

def is_solvable(puzzle):
    # Flatten the puzzle and remove the blank (0) for inversion calculation
    flat_puzzle = [tile for tile in puzzle if tile != 0]

    # Count inversions
    inversions = 0
    for i in range(len(flat_puzzle)):
        for j in range(i + 1, len(flat_puzzle)):
            if flat_puzzle[i] > flat_puzzle[j]:
                inversions += 1

    # Find the blank (0) row, counting from the bottom
    blank_index = puzzle.index(0)
    blank_row = (blank_index // 4) + 1  # Row number (1-indexed)

    # Calculate solvability
    return (inversions + blank_row) % 2 == 0


frame = Frame(3, 3,
                [1, 2, 3,
                     4, 5, 0,
                     6, 7, 8])

if not is_solvable(frame.game_board):
    print('unsolvable')
    exit()

direct = ['U', 'L', 'D', 'R']
queue = [frame]
while True:
    moved_frames = queue[0].get_moved_boards()
    if queue[0].game_board == [1, 2, 3, 4, 5, 6, 7, 8, 0]:
        print('found')
        exit()

    queue = queue[1:]
    print(moved_frames.keys())
    for direction, new_frame in moved_frames.items():
        if tuple(new_frame) in already_moved:
            pass

        else:

            queue = [Frame(3, 3, new_frame)] + queue
            already_moved.add(tuple(new_frame))
            t = len(already_moved)
            if t%3600 ==0:
                print(t/3600)




