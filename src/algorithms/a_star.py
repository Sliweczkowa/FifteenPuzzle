from collections import deque

from src.frame import Frame


def a_star(frame: Frame, id_of_heuristic: int, weight: float) -> list[chr]:

    visited = set()

    row_no = frame.row_count
    column_no = frame.column_count

    # weight should be a number between 0 and 1

    queue = deque()
    queue.append((frame, 0, []))

    while not queue[0][0].validate_win():

        # Get possible moves
        starting_frame = queue.popleft()
        new_frame_boards_and_moves = list(starting_frame[0].get_moved_boards().items())
        old_frame_moves = starting_frame[2]

        visited.add(tuple(starting_frame[0].game_board))

        for move_chr, board in new_frame_boards_and_moves:

            if tuple(board) in visited:
                continue

            # Calculate heuristic - distance of every tile from win position
            h = 0
            for index, tile_number in enumerate(board):
                if tile_number != 0:
                    tile_pos = divmod(index, column_no)  # current position
                    tile_win_pos = divmod(tile_number - 1, column_no)  # p.ex. tile "1" at index 0
                    if id_of_heuristic == 0:
                        x = abs(tile_win_pos[0] - tile_pos[0])
                        y = abs(tile_win_pos[1] - tile_pos[1])
                        manhattan_distance = x + y
                        h += manhattan_distance
                    elif id_of_heuristic == 1:
                        x = abs(tile_win_pos[0] - tile_pos[0])
                        y = abs(tile_win_pos[1] - tile_pos[1])
                        if x > y:
                            diagonal_shortcut = 14 * y + 10 * (x - y)
                        else:
                            diagonal_shortcut = 14 * x + 10 * (y - x)
                        h += diagonal_shortcut
                    elif id_of_heuristic == 2:
                        if tile_pos[0] != tile_win_pos[0] or tile_pos[1] != tile_win_pos[1]:
                            h += 1

            # Calculate estimate of total cost
            frame = Frame(r=row_no, c=column_no, vals=board, cost=starting_frame[0].cost + 1)
            total_cost = ((1 - weight) * frame.cost) + (weight * h)

            # Insert to queue
            inserted = False
            for index, total_cost_queue in enumerate(queue):
                total_cost_queue = total_cost_queue[1]
                if total_cost < total_cost_queue:
                    queue.insert(index, (frame, total_cost, old_frame_moves + [move_chr]))
                    inserted = True
                    break
            if not inserted:
                queue.append((frame, total_cost, old_frame_moves + [move_chr]))

    return queue.popleft()[2]


# fr0 = Frame(3, 3, [1, 2, 3, 4, 5, 6, 7, 0, 8])
# fr1 = Frame(3, 3, [1, 3, 6, 5, 2, 0, 4, 7, 8])
fr2 = Frame(3, 3, [1, 8, 2, 0, 4, 3, 7, 6, 5])
# fr3 = Frame(4, 4, [11, 4, 10, 7, 0, 3, 9, 2, 15, 1, 14, 5, 12, 13, 6, 8])
# result_bfs = bfs2(fr1, ['R', 'L', 'D', 'U'])
# print(result_bfs)
result = a_star(frame=fr2, id_of_heuristic=0, weight=0.5)
print(len(result))
print(result)

i = 0
