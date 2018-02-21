#! /usr/bin/env python3.6

#import tkinter as tk
#from tkinter import ttk

def PrintBoard(tkinter_canvas, width = 255, height = 255, row_num = 3, col_num = 3):
    x_list = [0]
    y_list = [0]
    #print rows of the board
    for line_num in range(0, (row_num-1)):
        x0 = 0
        y0 = (height/row_num)*(line_num+1)
        x1 = width
        y1 = (height/row_num)*(line_num+1)
        tkinter_canvas.create_line(x0, y0, x1, y1, fill = "yellow", width = 10)
        y_list.append(y0)

    #print columns of the board
    for line_num in range(0, (col_num-1)):
        x0 = (width/col_num)*(line_num+1)
        y0 = 0
        x1 = (width/col_num)*(line_num+1)
        y1 = height
        tkinter_canvas.create_line(x0, y0, x1, y1, fill = "yellow", width = 10)
        x_list.append(x0)

    x_list.append(width)
    y_list.append(height)

    return(x_list, y_list)


if(__name__ == "__main__") :
    print("This PrintBoard.py is used standalone.")
else :
    print("This PrintBoard.py is used by being imported.")
