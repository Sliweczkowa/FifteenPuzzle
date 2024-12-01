import argparse

from src.algorithms.bfs import bfs
from src.frame import Frame

parser = argparse.ArgumentParser(conflict_handler='resolve')

parser.add_argument("-b", "--bfs", help="breadth-first search", type=str, metavar="order")
parser.add_argument("-d", "--dfs", help="depth-first search", type=str, metavar="order")
parser.add_argument("-i", "--idfs", help="iterative deepening DFS", type=str, metavar="order")
parser.add_argument("-h", "--bf", help="best-first strategy", type=int, metavar="id_of_heuristic")
parser.add_argument("-a", "--astar", help="A* strategy", type=int, metavar="id_of_heuristic")
parser.add_argument("-s", "--sma", help="SMA* strategy", type=int, metavar="id_of_heuristic")
parser.add_argument("-f", "--save", help="save output to text file", type=str, metavar="filename")

args = parser.parse_args()

# Row and column input
r, c = [int(x) for x in input().split(' ')]
# Board values input
str_list = []
for i in range(r):
    str_list += [int(x) for x in input().split(' ')]
# Frame creation
frame = Frame(r, c, str_list)

if args.bfs:
    bfs = bfs(frame, args.bfs)  # TODO: Switch for bfs2 (latin chrs) when ready
    print(len(bfs) - 1, '\n', bfs)

if args.dfs:
    # TODO: Implement depth-first search
    print("Info: depth-first search not implemented yet")

if args.idfs:
    # TODO: Implement iterative deepening DFS
    print("Info: iterative deepening DFS not implemented yet")

if args.bf:
    # TODO: Implement best-first strategy
    print("Info: best-first strategy not implemented yet")

if args.astar:
    # TODO: Implement A* strategy
    print("Info: A* strategy not implemented yet")

if args.sma:
    # TODO: Implement SMA* strategy
    print("Info: SMA* strategy not implemented yet")

if args.save:
    # TODO: Implement output saving
    print("Info: saving not implemented yet")
