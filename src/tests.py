import time

from src.algorithms.a_star import a_star
from src.algorithms.bfs2 import bfs2
from src.algorithms.dfs2 import dfs
from src.algorithms.idfs import idfs
from src.frame import Frame


def best_first_search(frame):
    return a_star(frame, 1, 1)


def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"{func.__name__} took {elapsed_time:.4f} seconds, in moves: {len(result)}")
        return result

    return wrapper


# Example usage with the a_star algorithm
@measure_time
def run_a_star(frame, param1, param2):
    return a_star(frame, param1, param2)


# Example usage with the idfs algorithm
@measure_time
def run_idfs(frame, order_of_moves, depth, depth_limit):
    return idfs(frame, order_of_moves, depth, depth_limit)


# Example usage with the dfs algorithm
@measure_time
def run_dfs(frame, order_of_moves):
    return dfs(frame, order_of_moves)


@measure_time
def run_bfs(frame, order_of_moves):
    return bfs2(frame, order_of_moves)


@measure_time
def run_best(frame):
    return best_first_search(frame)


# Example usage
f1 = Frame(3, 3, [1, 3, 6, 5, 2, 0, 4, 7, 8])
f2 = Frame(3, 3, [6, 2, 8, 5, 1, 7, 3, 4, 0])
f3 = Frame(3, 3, [3, 7, 4, 8, 1, 6, 5, 2, 0])
f4 = Frame(3, 3, [2, 5, 3, 6, 8, 7, 1, 4, 0])
f5 = Frame(3, 3, [7, 5, 1, 8, 4, 6, 2, 3, 0])
frames = [f1, f2, f3, f4, f5]
#
# for index, frame in enumerate(frames):
#     print(f"Frame {index + 1}")
#     run_dfs(frame, ['R', 'L', 'D', 'U'])
#     run_idfs(frame, ['R', 'L', 'D', 'U'], 0, 1)
#     run_bfs(frame, ['R', 'L', 'D', 'U'])
#     run_a_star(frame, 1, 0.5)
#     run_best(frame)

# a* with params:
for index, frame in enumerate(frames):

    for heuristics in (0, 1, 2):
        weight = 0.5
        print(f"Frame {index + 1} with heuristics {heuristics} and weight {weight}", end=" ")
        run_a_star(frame, heuristics, weight)
