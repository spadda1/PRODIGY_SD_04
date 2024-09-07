import pyautogui as pg
import numpy as np
import time

grid = []

# Collect grid input
while True:
    row = input('Row: ')
    if len(row) != 9:
        print("Each row must contain exactly 9 numbers.")
        continue
    
    try:
        ints = [int(n) for n in row]
    except ValueError:
        print("Please enter only numbers.")
        continue
    
    grid.append(ints)

    if len(grid) == 9:
        break
    print('Row ' + str(len(grid)) + ' Complete')

time.sleep(3)

def possible(x, y, n):
    for i in range(9):
        if grid[i][x] == n and i != y:
            return False
        
    for i in range(9):
        if grid[y][i] == n and i != x:
            return False
        
    x0 = (x // 3) * 3
    y0 = (y // 3) * 3
    for X in range(x0, x0 + 3):
        for Y in range(y0, y0 + 3):
            if grid[Y][X] == n:
                return False
    return True

def Print(matrix):
    str_fin = [str(num) for row in matrix for num in row]
    counter = []
    
    for num in str_fin:
        pg.press(num)
        pg.hotkey('right')
        counter.append(num)
        if len(counter) % 9 == 0:
            pg.hotkey('down')
            pg.hotkey('left', presses=9)

def solve():
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1, 10):
                    if possible(x, y, n):
                        grid[y][x] = n
                        solve()
                        grid[y][x] = 0
                return
    Print(grid)
    input('More?')

solve()
