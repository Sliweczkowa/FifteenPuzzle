import argparse

from src.algorithms.a_star import a_star
from src.algorithms.bfs2 import bfs2
from src.algorithms.dfs2 import dfs
from src.algorithms.idfs import idfs
from src.algorithms.sma import sma_star
from src.frame import Frame, save_boards_to_file

parser = argparse.ArgumentParser(conflict_handler='resolve')

parser.add_argument("-b", "--bfs", help="breadth-first search", type=str, metavar="order")
parser.add_argument("-d", "--dfs", help="depth-first search", type=str, metavar="order")
parser.add_argument("-i", "--idfs", help="iterative deepening DFS", type=str, metavar="order")
parser.add_argument("-h", "--bf", help="best-first strategy", type=str, metavar="id_of_heuristic")
parser.add_argument("-a", "--astar", help="A* strategy", type=str, metavar="id_of_heuristic")
parser.add_argument("-s", "--sma", help="SMA* strategy", type=str, metavar="id_of_heuristic")
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

# Check if board is solvable
if frame.is_solvable():
    result = []
else:
    print("-1")
    exit()

if args.bfs:
    result = bfs2(frame, list(args.bfs))

if args.dfs:
    result = dfs(frame, list(args.dfs))

if args.idfs:
    result = idfs(frame, list(args.idfs), 0, 1)

if args.bf:
    result = a_star(frame, int(args.bf), 1)  # Only heuristic part of a*

if args.astar:
    result = a_star(frame, int(args.astar), 0.5)

if args.sma:
    result = sma_star(frame, int(args.sma), 0.5, 100)

if len(result) == 0:
    print("-1")
else:
    print(len(result), '\n' + result)

if args.save:
    if result != -1 and result != []:
        save_boards_to_file(frame, result, args.save)
