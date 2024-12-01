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

Described program was tested using following *8 puzzle* and *15 puzzle* boards:

| Frame id | Row no. | Column no. | Board                       |
|----------|---------|------------|-----------------------------|
| 1        | 3       | 3          | [1, 3, 6, 5, 2, 0, 4, 7, 8] |
| 2        | 3       | 3          | [6, 2, 8, 5, 1, 7, 3, 4, 0] |
| 3        | 3       | 3          | [3, 7, 4, 8, 1, 6, 5, 2, 0] |
| 4        | 3       | 3          | [2, 5, 3, 6, 8, 7, 1, 4, 0] |
| 5        | 3       | 3          | [7, 5, 1, 8, 4, 6, 2, 3, 0] |


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

| Function |         |       |
|----------|---------|-------|
| bfs      | 18.2    | 0.712 |
| dfs      | 59159.4 | 14.77 |
| idfs     | 20.2    | 1.122 |
| best     | 40.2    | 0.014 |
| a_star   | 26.2    | 0.009 |
| smf_star | 40.2    | 0.008 |

| Function |       |       |
|----------|-------|-------|
| best     | 128.4 | 0.103 |
| a_star   | 102.8 | 1.221 |
| smf_star | 128.4 | 0.105 |
