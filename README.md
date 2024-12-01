# FifteenPuzzle

Project created for Lodz University of Technology "AI &amp; Expert Systems" course.

The program solves game *15 puzzle* using following pathfinding algorithms:

- breadth-first search
- depth-first search
- iterative deepening DFS
- best-first strategy
- A* strategy
- SMA* strategy

## Algorithms comparison

### Described program was tested using following *8 puzzle* and *15 puzzle* boards:

| Board 3x3                   |
|-----------------------------|
| [1, 3, 6, 5, 2, 0, 4, 7, 8] |
| [6, 2, 8, 5, 1, 7, 3, 4, 0] |
| [3, 7, 4, 8, 1, 6, 5, 2, 0] |
| [2, 5, 3, 6, 8, 7, 1, 4, 0] |
| [7, 5, 1, 8, 4, 6, 2, 3, 0] |

Here is a table for default arguments* run algorithms on 3x3 board:
For smf, a_star this means manhattan distance heuristics, and 0.5 weight for cost eval
on top of that smf uses limit 100 for queue.

### Execution for 3x3 board

| Frame | Function | Time (s) | Steps |
|-------|----------|----------|-------|
| 1     | smf_star | 0.000998 | 7     |
|       | dfs      | 22.0201  | 47617 |
|       | idfs     | 0.00399  | 7     |
|       | bfs      | 0.00199  | 7     |
|       | best     | 0.0      | 7     |
|       | a_star   | 0.0      | 7     |
| 2     | smf_star | 0.00798  | 44    |
|       | dfs      | 17.0454  | 61796 |
|       | idfs     | 3.5964   | 30    |
|       | bfs      | 0.9794   | 22    |
|       | best     | 0.0389   | 44    |
|       | a_star   | 0.01496  | 44    |
| 3     | smf_star | 0.01097  | 50    |
|       | dfs      | 13.5957  | 65036 |
|       | idfs     | 0.8476   | 24    |
|       | bfs      | 1.3462   | 24    |
|       | best     | 0.00898  | 50    |
|       | a_star   | 0.01396  | 26    |
| 4     | smf_star | 0.00798  | 46    |
|       | dfs      | 8.8969   | 57702 |
|       | idfs     | 1.0650   | 26    |
|       | bfs      | 1.1800   | 24    |
|       | best     | 0.00895  | 46    |
|       | a_star   | 0.00698  | 32    |
| 5     | smf_star | 0.01099  | 54    |
|       | dfs      | 12.2932  | 63646 |
|       | idfs     | 0.09899  | 14    |
|       | bfs      | 0.04992  | 14    |
|       | best     | 0.01199  | 54    |
|       | a_star   | 0.00701  | 22    |

### Average number of steps and time of execution for 3x3 board

| Function |         |       |
|----------|---------|-------|
| bfs      | 18.2    | 0.712 |
| dfs      | 59159.4 | 14.77 |
| idfs     | 20.2    | 1.122 |
| best     | 40.2    | 0.014 |
| a_star   | 26.2    | 0.009 |
| smf_star | 40.2    | 0.008 |

### Execution for 4x4 board

During this testing, we dropped dfs, idfs and bfs algorithm due to memory and time constraints.
While it is possible to solve simple boards, that require less then 20 steps, for more complex boards
it is too slow and memory consuming.

| Frame | Function Name | Execution Time (s)   | Step Number |
|-------|---------------|----------------------|-------------|
| 1     | run_smf_star  | 0.04288601875305176  | 141         |
| 1     | run_best      | 0.03593087196350098  | 141         |
| 1     | run_a_star    | 0.12614083290100098  | 97          |
| 2     | run_smf_star  | 0.2293872833251953   | 124         |
| 2     | run_best      | 0.24032998085021973  | 124         |
| 2     | run_a_star    | 0.18952417373657227  | 88          |
| 3     | run_smf_star  | 0.04883694648742676  | 159         |
| 3     | run_best      | 0.04587721824645996  | 159         |
| 3     | run_a_star    | 5.695905447006226    | 137         |
| 4     | run_smf_star  | 0.06582427024841309  | 92          |
| 4     | run_best      | 0.06183433532714844  | 92          |
| 4     | run_a_star    | 0.019920825958251953 | 88          |
| 5     | run_smf_star  | 0.13566303253173828  | 126         |
| 5     | run_best      | 0.1326465606689453   | 126         |
| 5     | run_a_star    | 0.07380199432373047  | 104         |

### Average number of steps and time of execution for 3x3 board

| Function |       |       |
|----------|-------|-------|
| best     | 128.4 | 0.103 |
| a_star   | 102.8 | 1.221 |
| smf_star | 128.4 | 0.105 |

### Execution for different weights for A* algorithm

| Frame | Time (s) | Function Name | Execution Time (s)   | Step Number |
|-------|----------|---------------|----------------------|-------------|
| 1     | 0.5      | run_a_star    | 0.12269973754882812  | 97          |
| 1     | 0.6      | run_a_star    | 0.0259249210357666   | 85          |
| 1     | 0.7      | run_a_star    | 0.009981870651245117 | 77          |
| 1     | 0.8      | run_a_star    | 0.0717766284942627   | 127         |
| 1     | 0.9      | run_a_star    | 0.0468745231628418   | 129         |
| 1     | 1        | run_a_star    | 0.03394198417663574  | 141         |
| 2     | 0.5      | run_a_star    | 0.18846368789672852  | 88          |
| 2     | 0.6      | run_a_star    | 0.06981277465820312  | 88          |
| 2     | 0.7      | run_a_star    | 0.16259407997131348  | 124         |
| 2     | 0.8      | run_a_star    | 0.27537012100219727  | 124         |
| 2     | 0.9      | run_a_star    | 0.3729739189147949   | 158         |
| 2     | 1        | run_a_star    | 0.2403576374053955   | 124         |
| 3     | 0.5      | run_a_star    | 5.646948337554932    | 137         |
| 3     | 0.6      | run_a_star    | 0.18952512741088867  | 147         |
| 3     | 0.7      | run_a_star    | 0.13361549377441406  | 153         |
| 3     | 0.8      | run_a_star    | 0.08679580688476562  | 149         |
| 3     | 0.9      | run_a_star    | 0.08178091049194336  | 149         |
| 3     | 1        | run_a_star    | 0.0468745231628418   | 159         |
| 4     | 0.5      | run_a_star    | 0.019949674606323242 | 88          |
| 4     | 0.6      | run_a_star    | 0.021938800811767578 | 88          |
| 4     | 0.7      | run_a_star    | 0.02889418601989746  | 88          |
| 4     | 0.8      | run_a_star    | 0.03393745422363281  | 96          |
| 4     | 0.9      | run_a_star    | 0.050835609436035156 | 96          |
| 4     | 1        | run_a_star    | 0.06386017799377441  | 92          |
| 5     | 0.5      | run_a_star    | 0.07875847816467285  | 104         |
| 5     | 0.6      | run_a_star    | 0.05887174606323242  | 118         |
| 5     | 0.7      | run_a_star    | 0.12364053726196289  | 118         |
| 5     | 0.8      | run_a_star    | 0.04547119140625     | 126         |
| 5     | 0.9      | run_a_star    | 0.0912623405456543   | 126         |
| 5     | 1        | run_a_star    | 0.13602876663208008  | 126         |

### Average number of steps and time of execution for different weights

| Weight | Time (s)            | Steps |
|--------|---------------------|-------|
| 0.5    | 1.2113639831542968  | 102.8 |
| 0.6    | 0.07321467399597167 | 105.2 |
| 0.7    | 0.09174523353576661 | 112   |
| 0.8    | 0.10267024040222168 | 124.4 |
| 0.9    | 0.1287454605102539  | 131.6 |
| 1      | 0.10421261787414551 | 128.4 |

### Exeuction of a* for different heuristics, with 0.7 weight

1 denotes manhattan, and 0 diagonal distance.

| Frame | State | Time (s)             | Steps |
|-------|-------|----------------------|-------|
| 1     | 0     | 1.3833017349243164   | 63    |
| 1     | 1     | 0.009972572326660156 | 77    |
| 2     | 0     | 1.683500051498413    | 62    |
| 2     | 1     | 0.1545853614807129   | 124   |
| 3     | 0     | 10.708368062973022   | 61    |
| 3     | 1     | 0.12868404388427734  | 153   |
| 4     | 0     | 26.735516786575317   | 72    |
| 4     | 1     | 0.03487539291381836  | 88    |
| 5     | 0     | 0.383974552154541    | 70    |
| 5     | 1     | 0.14860272407531738  | 118   |

# Average number of steps and time of execution different heuristics

| Weight | Time (s)            | Steps |
|--------|---------------------|-------|
| 0      | 8.178932237625123   | 65.6  |
| 1      | 0.09534401893615722 | 112   |

## Summary

### Summary of Each Algorithm

1. **Breadth-First Search (BFS)**:
    - BFS explores all possible paths level by level, making it very slow for larger puzzles due to the need to explore
      all options. It is not ideal for larger puzzles, as it consumes a lot of memory and time, especially in more
      complex scenarios.

2. **Depth-First Search (DFS)**:
    - DFS explores a single path deeply before backtracking. While it can be efficient in certain cases, it often fails
      to find the optimal solution and may get stuck in deep or long paths. It is inefficient for moderately-sized
      problems due to the excessive number of steps.

3. **Iterative Deepening DFS (IDFS)**:
    - IDFS combines the depth-first approach with a systematic increase in the depth limit. This algorithm is more
      memory-efficient than BFS and guarantees finding the optimal solution. However, it is still slower than other
      strategies.
4. **Best-First Search (Best)**:
    - Best-First Search uses a heuristic to explore the most promising nodes first. While it is faster than BFS and DFS,
      it does not guarantee an optimal solution and may miss paths that would lead to the best outcome. It is fast but
      limited in guaranteeing optimality.

5. **A\* Search**:
    - A* is one of the most efficient algorithms for pathfinding because it uses a heuristic to find the optimal
      solution efficiently. It balances exploration with exploitation and finds the best solution while being faster and
      more memory-efficient than BFS and DFS. A* is ideal for larger puzzles, balancing accuracy and speed.

6. **SMA\* (Simplified Memory-Bounded A\*)**:
    - SMA* is a variant of A* designed to work within a limited memory space. It uses a memory-efficient search method
      while still trying to find the best path. While slower than A*, it is much more efficient when memory is limited.

### Performance on 4x4 Board:

For the 4x4 board, BFS, DFS, and IDFS were omitted due to their high memory usage and execution time. A* and SMA* were
the preferred algorithms, with A* being slower compared to SMA*. The higher complexity of the 4x4 puzzle makes these
algorithms more efficient.

### Heuristic Testing for A* Algorithm:

Testing different heuristics (Manhattan vs Diagonal) with varying weights showed a trade-off between speed and
optimality. Manhattan distance provided slower results compared to diagonal distance, and weights closer to 1 seemed to
balance the speed and accuracy better.

In summary, **A*** is the most efficient for small puzzles and guarantees optimality, while **SMA*** offers memory
efficiency at the cost of slightly slower performance. **Best-First** can be useful when you prioritize speed over
optimality. **DFS**, **BFS**, and **IDFS** are generally not suited for larger or more complex puzzles due to their high
memory and time requirements.



