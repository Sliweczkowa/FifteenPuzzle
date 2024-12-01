# 8 puzzle
from src.frame import Frame
from src.algorithms.bfs2 import bfs2
from src.algorithms.dfs2 import dfs
from src.algorithms.idfs import idfs
from src.algorithms.a_star import a_star

print("dupa")


f1 = Frame(3,3,[1, 2, 3, 4, 5, 6, 7, 0, 8])
# f1 = Frame(3,3,[8,5,1,4,3,7,2,6])

def run_algos(frame):

    #
    # _bfs = (bfs2(frame, ['U', 'D', 'L', 'R']))
    # _astr =  a_star(frame,1,1)
    # _dfs = (dfs(frame, ['U', 'D', 'L', 'R']))
    _idfs = (idfs(frame,['R', 'D', 'L', 'U'],0,1))

    # print(len(_bfs))
    # print(len(_astr))
    # print(len(_dfs))
    print(len(_idfs))

run_algos(f1)