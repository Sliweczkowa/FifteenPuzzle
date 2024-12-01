import time

from src.algorithms.a_star import a_star
from src.algorithms.bfs2 import bfs2
from src.algorithms.dfs2 import dfs
from src.algorithms.idfs import idfs
from src.algorithms.sma import sma_star
from src.frame import Frame


def best_first_search(frame):
    return a_star(frame, 1, 1)


def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        # print(f"Function {func.__name__} took {elapsed_time} seconds and took {len(result)} steps")
        print(f"{func.__name__},{elapsed_time},{len(result)}")
        return func.__name__, elapsed_time, len(result)

    return wrapper


# Example usage with the a_star algorithm
@measure_time
def run_a_star(frame, param1, param2):
    return a_star(frame, param1, param2)


@measure_time
def run_smf_star(frame, param1, param2):
    return sma_star(frame, param1, param2, 1000)


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


b1 = Frame(4, 4, [8, 0, 7, 15, 1, 10, 11, 6, 14, 9, 2, 13, 3, 5, 4, 12])
b2 = Frame(4, 4, [0, 9, 11, 7, 15, 1, 2, 5, 14, 13, 6, 4, 3, 8, 12, 10])
b3 = Frame(4, 4, [13, 9, 12, 7, 6, 4, 3, 8, 11, 14, 2, 0, 1, 15, 10, 5])
b4 = Frame(4, 4, [4, 15, 0, 6, 1, 14, 12, 2, 10, 8, 7, 3, 11, 9, 5, 13])
b5 = Frame(4, 4, [6, 10, 3, 15, 7, 8, 12, 9, 13, 2, 0, 14, 4, 5, 11, 1])

# Example usage
f1 = Frame(3, 3, [1, 3, 6, 5, 2, 0, 4, 7, 8])
f2 = Frame(3, 3, [6, 2, 8, 5, 1, 7, 3, 4, 0])
f3 = Frame(3, 3, [3, 7, 4, 8, 1, 6, 5, 2, 0])
f4 = Frame(3, 3, [2, 5, 3, 6, 8, 7, 1, 4, 0])
f5 = Frame(3, 3, [7, 5, 1, 8, 4, 6, 2, 3, 0])
# frames = [f1, f5, f2, f3, f4]
frames = [b1, b2, b3, b4, b5]
# for index, frame in enumerate(frames):
#     print(f"{index + 1}", end=",")
#     run_smf_star(frame, 1, 1)
#     # run_dfs(frame, ['R', 'L', 'D', 'U'])
#     # run_idfs(frame, ['R', 'L', 'D', 'U'], 0, 1)
#     # run_bfs(frame, ['R', 'L', 'D', 'U'])
#     print(f"{index + 1}", end=",")
#     run_best(frame)
#     print(f"{index + 1}", end=",")
#     run_a_star(frame, 1, 0.5)

print("frame,heuristics,weight,func,time,steps")

# # a* with params:
for index, frame in enumerate(frames):
    for heuristics in (0, 1):
        weight = 0.7
    # print(f"Frame {index + 1} with heuristics {heuristics} and weight {weight}", end=" ")
        print(f"{index + 1},{heuristics},{weight},", end="")
        run_a_star(frame, heuristics, weight)

#
# Generate all permutations of the directions
# directions = ['R', 'L', 'D', 'U']
# permutations = list(itertools.permutations(directions))
#
# for index, frame in enumerate(frames):
#     print(f"Frame {index + 1}")
#
#     for perm in permutations:
#         print(f"Testing with permutation: {perm}")
#         run_dfs(frame, ['R', 'L', 'D', 'U'])
#         run_idfs(frame, ['R', 'L', 'D', 'U'], 0, 1)
#         run_bfs(frame, ['R', 'L', 'D', 'U'])
#         run_best(frame)
#         run_a_star(frame, 1, 1)
#         run_smf_star(frame, 1, 1)
#
#
