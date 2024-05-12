from Sudoku import sudoku 
import numpy as np 

game_sudoku = sudoku()
game_sudoku.read_data("data.txt")
game_sudoku.AC3_solve()
