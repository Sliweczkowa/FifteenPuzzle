from queue import Queue

from src.frame import Frame


# TODO: do not repeat taken path
def bfs(board: Frame, order: set[chr]) -> list[chr] | int:
    queue = Queue()  # Queue of unchecked moves
    moves = []  # Output list of moves
    chrs = []
    coords = []

    # Get blank coordinates
    (blank_row, blank_col) = board.get_blank_pos()

    # Check for win
    while board.validate_win() is False:

        # Get possible moves of blank
        legal_moves = board.get_legal_moves(blank_row, blank_col)  # unordered set of tuples

        # TODO: sort moves by 'order' parameter and output to ordered array

        # Get possible new coordinates of blank
        legal_coords = [(m[0]+blank_row, m[1]+blank_col) for m in legal_moves]

        # Get possible moves of free pieces
        dictionary = {
            (-1, 0): 'D',
            (1, 0): 'U',
            (0, -1): 'R',
            (0, 1): 'L'
        }
        legal_chrs = [dictionary.get(m) for m in legal_moves]

        # Push possible coordinates of blank
        for l in legal_coords:
            queue.put(l)

        # Get next move
        next_blank = queue.get()

        # Change blank coordinates
        blank_row, blank_col = next_blank[0], next_blank[1]

        # Puzzle has not been solved
        if queue.empty() is True:
            return -1

    coords.insert(0, (blank_row, blank_col))


    moves.insert(0, legal_moves[legal_coords.index(coords[0])])
    chrs.insert(0, legal_chrs[legal_coords.index(coords[0])])

    return chrs


bfs(Frame(3, 3, [5, 4, 8, 6, 0, 1, 7, 2, 3]), 1)
