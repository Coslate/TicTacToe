#! /usr/bin/env python3.6
'''
#Author  : Coslate
#Purpose : This progriam is a TicTacToe game.
#Date    : 2017/12/02
'''

#self define function
import package_used.setting as setting
import package_used.mouse_func.mouse as mouse_function

#main function
def main():
    '''main function'''

    setting.init()

    #print the board
    setting.tictactoe_ob.PrintBoard()
    setting.x_list = setting.tictactoe_ob.GetXList()
    setting.y_list = setting.tictactoe_ob.GetYList()

    #get the updated canvas from tictactoe_ob
    setting.window_canvas = setting.tictactoe_ob.GetCanvas()

    while True:
        setting.window_canvas.bind("<Button-1>", mouse_function.LeftMouseCallBack)
        setting.window_canvas.bind("<Button-3>", mouse_function.RightMouseCallBack)
        setting.window_canvas.bind("<Button-2>", mouse_function.MiddleMouseCallBack)
        setting.window_canvas = setting.tictactoe_ob.GetCanvas()
        setting.window_canvas.pack()
        setting.window_top.update()

    #window_top.mainloop()

#---------------Execution---------------#
if __name__ == '__main__':
    main()
