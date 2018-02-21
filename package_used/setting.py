#! /usr/bin/env python3.6

import tkinter as tk
from tkinter import ttk
from . import tictactoe

#---------------Global variable---------------#
def init():
    global window_top
    global window_canvas
    global tictactoe_ob
    global frame_width
    global frame_height
    global board_row_num
    global board_col_num
    global x_list
    global y_list
    global win_conn_num

    window_top = tk.Tk()
    window_top.title("My first Tk GUI")
    frame_width = 640
    frame_height = 480
    board_row_num = 3
    board_col_num = 3
    x_list = []
    y_list = []
    win_conn_num = 3

    #Create Canvas
    window_canvas = tk.Canvas(window_top, bg = "pink", height = frame_height, width = frame_width)
    #Create tictactoe object
    tictactoe_ob = tictactoe.TicTacToe(window_canvas, frame_height, frame_width, board_row_num, board_col_num)

if(__name__ == "__main__") :
    print("This setting.py is used standalone.")
else :
    print("This setting.py is used by being imported.")
