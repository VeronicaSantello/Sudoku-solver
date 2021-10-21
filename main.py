# -*- coding: utf-8 -*-
import functions
import functions1
import copy
import numpy as np


# easy sudoku (default input)
matrix = np.array([[3, 7, 0, 5, 0, 0, 0, 0, 6],
            [0, 0, 0, 3, 6, 0, 0, 1, 2],
            [0, 0, 0, 0, 9, 1, 7, 5, 0],
            [0, 0, 0, 1, 5, 4, 0, 7, 0],
            [0, 0, 3, 0, 7, 0, 6, 0, 0],
            [0, 5, 0, 6, 3, 8, 0, 0, 0],
            [0, 6, 4, 9, 8, 0, 0, 0, 0],
            [5, 9, 0, 0, 2, 6, 0, 0, 0],
            [2, 0, 0, 0, 0, 5, 0, 6, 4]])

# hard sudoku
matrix2 = np.array([[0, 4, 3, 0, 0, 7, 8, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 4],
            [0, 6, 8, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 3, 1, 0, 8, 6],
            [0, 0, 9, 2, 0, 5, 1, 0, 0],
            [4, 8, 0, 7, 9, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 6, 5, 0],
            [2, 0, 0, 0, 0, 0, 0, 0, 8],
            [0, 0, 5, 8, 0, 0, 2, 1, 0],
            ])

# N.B. create always a copy of matrix that you want solve!!!!!!!!
matrix1 = copy.deepcopy(matrix)


# if you want change input, you must change all the parameters only for backtracking algorithm
print("===========================CP AND BACKTRACKING==============================")
domains = functions.define_domains(matrix)
print("---------- INITIAL BOARD----------")
functions.print_board(matrix)
functions.solve(matrix, domains)
print("---------- FINAL BOARD----------")
functions.print_board(matrix)


# never change parameters
print("===========================RELAXATION LABELING==============================")
p = functions1.define_distributions(domains)
print("---------------MONITORING----------------")
functions1.solve(matrix1, p)



