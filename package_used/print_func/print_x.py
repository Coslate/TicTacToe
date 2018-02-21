#! /usr/bin/env python3.6

#import tkinter as tk
#from tkinter import ttk

def PrintX(tkinter_canvas, lx0, ly0, lx1, ly1, rx0, ry0, rx1, ry1):
    tkinter_canvas.create_line(lx0, ly0, lx1, ly1, fill = "#000", width = 10)
    tkinter_canvas.create_line(rx0, ry0, rx1, ry1, fill = "#000", width = 10)

if(__name__ == "__main__") :
    print("This PrintX.py is used standalone.")
else :
    print("This PrintX.py is used by being imported.")
