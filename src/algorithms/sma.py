from collections import deque
from src.frame import Frame

def sma_star(frame: Frame, id_of_heuristic: int, weight: float, memory_limit: int) -> list[chr]:
    visited = set()
    row_no = frame.row_count
    column_no = frame.column_count

    # Deque to store nodes with their total cost
    queue = deque()
    queue.append((0, frame, []))

    while queue:
        total_cost, current_frame, path = queue.popleft()

        if current_frame.validate_win():
            return path

        visited.add(tuple(current_frame.game_board))
        new_frame_boards_and_moves = list(current_frame.get_moved_boards().items())

        for move_chr, board in new_frame_boards_and_moves:
            if tuple(board) in visited:
                continue

            # Calculate heuristic
            h = 0
            for index, tile_number in enumerate(board):
                if tile_number != 0:
                    tile_pos = divmod(index, column_no)
                    tile_win_pos = divmod(tile_number - 1, column_no)
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

            # Calculate total cost
            new_frame = Frame(r=row_no, c=column_no, vals=board, cost=current_frame.cost + 1)
            new_total_cost = ((1 - weight) * new_frame.cost) + (weight * h)

            # Insert new node into the deque in the correct position based on total cost
            inserted = False
            for index, (cost, _, _) in enumerate(queue):
                if new_total_cost < cost:
                    queue.insert(index, (new_total_cost, new_frame, path + [move_chr]))
                    inserted = True
                    break
            if not inserted:
                queue.append((new_total_cost, new_frame, path + [move_chr]))

            # If memory limit is reached, remove the node with the highest cost
            if len(queue) > memory_limit:
                queue.pop()

    return []