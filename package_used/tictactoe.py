#! /usr/bin/env python3.6

from .print_func import print_board

class TicTacToe:
    def __init__(self, window_canvas, frame_height, frame_width, board_row_num, board_col_num):
        self.__frame_height = frame_height
        self.__frame_width = frame_width
        self.__board_row_num = board_row_num
        self.__board_col_num = board_col_num
        self.__window_canvas = window_canvas
        self.__x_list = []
        self.__y_list = []
        self.__O_setXY_list = []
        self.__X_setXY_list = []

    def PrintBoard(self):
        (self.__x_list, self.__y_list) = print_board.PrintBoard(self.__window_canvas, self.__frame_width, self.__frame_height, self.__board_row_num, self.__board_col_num)

    def GetCanvas(self):
        return self.__window_canvas

    def GetFrameHeight(self):
        return self.__frame_height

    def GetFrameWidth(self):
        return self.__frame_width

    def GetBoardRowNum(self):
        return self.__board_row_num

    def GetBoardColNum(self):
        return self.__board_col_num

    def GetXList(self):
        return self.__x_list

    def GetYList(self):
        return self.__y_list

    def GetOXYSetPos(self):
        return self.__O_setXY_list

    def GetXXYSetPos(self):
        return self.__X_setXY_list

    def SaveOXYSetPos(self, x_pos, y_pos):
        self.__O_setXY_list.append((x_pos, y_pos))

    def SaveXXYSetPos(self, x_pos, y_pos):
        self.__X_setXY_list.append((x_pos, y_pos))

    def CheckOXYSetPosExist(self, x_pos, y_pos):
        s = set(self.__O_setXY_list)
        if((x_pos, y_pos) in s):
            return True
        else:
            return False

    def CheckXXYSetPosExist(self, x_pos, y_pos):
        s = set(self.__X_setXY_list)
        if((x_pos, y_pos) in s):
            return True
        else:
            return False

    def WinDetermination(self, win_conn_num):


        return

    def DeleteXYList(self):
        del self.__O_setXY_list[::1]
        del self.__X_setXY_list[::1]

if(__name__ == "__main__") :
    print("This tictactoe.py is used standalone.")
else :
    print("This tictactoe.py is used by being imported.")
