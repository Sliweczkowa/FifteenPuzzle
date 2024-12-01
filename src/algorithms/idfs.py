from src.frame import Frame




def idfs(frame: Frame, order_of_moves, depth, depth_limit):

    already_moved = set()

    def _idfs(frame: Frame, order_of_moves, depth, depth_limit):

        if depth > depth_limit:
            return False

        already_moved.add(tuple(frame.game_board))
        moved_frames = frame.get_moved_boards()

        if frame.validate_win():
            return frame.moved

        for direction in order_of_moves:
            if direction not in moved_frames:
                continue
            new_frame = moved_frames[direction]
            if tuple(new_frame) in already_moved:
                continue
            additive = frame.moved + direction
            return _idfs(Frame(frame.row_count, frame.column_count, new_frame, additive), order_of_moves, depth + 1,
                 depth_limit)

    while True:
        r = _idfs(frame, order_of_moves,depth,depth_limit)
        depth_limit += 1
        already_moved.clear()

        if r:
            return r
