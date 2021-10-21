# -*- coding: utf-8 -*-
import copy


def define_domains(matrix):
    domains = []
    for i in range(0, 9):
        for j in range(0, 9):
            list = []
            if matrix[i][j] == 0:
                for k in range(1, 10):
                    if valid(matrix, k, (i, j)):
                        list.append(k)
            else:
                list.append(matrix[i][j])

            domains.append(list)

    return domains


def solve(matrix, dom):
    find = find_empty(matrix)
    if not find:
        return True
    else:
        row, col = find
    if [] in dom:
        return False

    for i in dom[row*9 + col]:
        matrix[row][col] = i
        if solve(matrix, modify_domains(matrix, copy.deepcopy(dom), i, (row, col))):
            return True

        matrix[row][col] = 0

    return False


def modify_domains(matrix, dom, num, pos):
    # Check all values on the same row
    for i in range(len(matrix[0])):
        if pos[1] != i and num in dom[pos[0]*9 + i]:
            dom[pos[0]*9 + i].remove(num)

    # Check all values on the same column
    for i in range(len(matrix)):
        if pos[0] != i and num in dom[pos[1] + i*9]:
            dom[pos[1] + i*9].remove(num)

    # Check all values on the same box
    box_x = pos[0] // 3
    box_y = pos[1] // 3

    for i in range(box_x * 3, box_x * 3 + 3):
        for j in range(box_y * 3, box_y * 3 + 3):
            if (i, j) != pos and num in dom[j + i*9]:
                dom[j + i*9].remove(num)

    return dom


def valid(matrix, num, pos):
    # Check all values on the same row
    for i in range(len(matrix[0])):
        if matrix[pos[0]][i] == num and pos[1] != i:
            return False

    # Check all values on the same column
    for i in range(len(matrix)):
        if matrix[i][pos[1]] == num and pos[0] != i:
            return False

    # Check all values on the same box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if matrix[i][j] == num and (i,j) != pos:
                return False

    return True


def print_board(matrix):
    for i in range(len(matrix)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(matrix[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(matrix[i][j])
            else:
                print(str(matrix[i][j]) + " ", end="")


def find_empty(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                return i, j  # row, col

    return None