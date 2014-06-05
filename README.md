Sudoku-Solver
=============

Solves sudoku puzzles

Basic Overview
--------------

Sudoku solver will take any given sudoku game and solve it. The solution will print the completed sudoku grid along with the amount of time it took to find the solution.

1. Use dictionary to represent each square in sudoku grid.
2. All square values initialized to '123456789' to represent possible values.
3. Known square keys set to provided digits (1 digit per square).
4. Examine square's row, column, and block to remove digits from square keys' strings.
5. Repeat.
6. Print final grid and solve time.
