from collections import deque

from src.frame import Frame


def a_star(frame: Frame, order_of_moves: list[chr], weight: float) -> list[chr]:
    visited = set()
    row_no = frame.row_count
    column_no = frame.column_count

    g = 0
    # weight should be a number between 0 and 1

    queue = deque()
    queue.append((frame, 0, []))

    while not queue[0][0].validate_win():
        visited.add(tuple(queue[0][0].game_board))


        # Increment actual cost

        # Get possible moves
        starting_frame = queue.popleft()
        starting_frame[0].cost += 1
        new_frame_boards_and_moves = list(starting_frame[0].get_moved_boards().items())
        old_frame_moves = starting_frame[2]

        for move_chr, board in new_frame_boards_and_moves:
            if tuple(board) in visited:
                continue
            h = 0
            # Calculate heuristic - distance of every tile from win position
            for index, tile_number in enumerate(board):
                if tile_number != 0:
                    tile_pos = divmod(index, column_no)  # current position
                    tile_win_pos = divmod(tile_number - 1, column_no)  # p.ex. tile "1" at index 0
                    distance = abs(tile_win_pos[0] - tile_pos[0]) + abs(tile_win_pos[1] - tile_pos[1])
                    h += distance

            # Calculate estimate of total cost and insert
            frame = Frame(row_no, column_no, board,cost=starting_frame[0].cost)
            # print(frame.cost)
            total_cost = ((1 - weight) * starting_frame[0].cost) + (weight * h)
            inserted = False
            for index, total_cost_queue in enumerate(queue):
                total_cost_queue = total_cost_queue[1]
                if total_cost < total_cost_queue:
                    queue.insert(index, (frame, total_cost, [move_chr] + old_frame_moves))
                    inserted = True
                    break
            if not inserted:
                queue.append((frame, total_cost, old_frame_moves + [move_chr]))

    print(len(visited))
    print(queue[0][0].game_board)
    return queue.popleft()[2]


# fr0 = Frame(3, 3, [1, 2, 3, 4, 5, 6, 7, 0, 8])
# fr1 = Frame(3, 3, [1, 3, 6, 5, 2, 0, 4, 7, 8])
fr1 = Frame(4, 4, [11,4,10,7,0,3,9,2,15,1,14,5,12,13,6,8])
# result_bfs = bfs2(fr1, ['R', 'L', 'D', 'U'])
# print(result_bfs)
# print(result_bfs)
result = a_star(frame=fr1, order_of_moves=[], weight=0.9)
print(len(result))
# result1 = a_star(frame=fr1, order_of_moves=[], weight=0.5)
# print(len(result1))

print(result)
# print(result1)

i = 0
