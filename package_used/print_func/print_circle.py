#! /usr/bin/env python3.6

#import tkinter as tk
#from tkinter import ttk

def PrintCircle(tkinter_canvas, coord):
    Circle = tkinter_canvas.create_oval(coord, fill = "#BFF")


if(__name__ == "__main__") :
    print("This PrintCircle.py is used standalone.")
else :
    print("This PrintCircle.py is used by being imported.")
