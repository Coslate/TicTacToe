#! /usr/bin/env python3.6

from ..cal_func import calculate
from ..print_func import print_circle
from ..print_func import print_x
from .. import setting

#---------------Global function---------------#
def LeftMouseCallBack(event):
    (x0, y0, x1, y1, get_x_pos, get_y_pos) = calculate.CalPrintCirclePt(event.x, event.y, setting.x_list, setting.y_list)
    if((not(setting.tictactoe_ob.CheckOXYSetPosExist(get_x_pos, get_y_pos))) and (not(setting.tictactoe_ob.CheckXXYSetPosExist(get_x_pos, get_y_pos)))):
        coord = x0, y0, x1, y1
        print_circle.PrintCircle(setting.window_canvas, coord)
        setting.tictactoe_ob.SaveOXYSetPos(get_x_pos, get_y_pos)
        setting.tictactoe_ob.WinDetermination(setting.win_conn_num)

        o_xy_set_list = setting.tictactoe_ob.GetOXYSetPos()
        PrintSettingList(o_xy_set_list, "o_xy_set_list")

def RightMouseCallBack(event):
    (lx0, ly0, lx1, ly1, rx0, ry0, rx1, ry1, get_x_pos, get_y_pos) = calculate.CalPrintXPt(event.x, event.y, setting.x_list,setting. y_list)
    if((not(setting.tictactoe_ob.CheckOXYSetPosExist(get_x_pos, get_y_pos))) and (not(setting.tictactoe_ob.CheckXXYSetPosExist(get_x_pos, get_y_pos)))):
        print_x.PrintX(setting.window_canvas, lx0, ly0, lx1, ly1, rx0, ry0, rx1, ry1)
        setting.tictactoe_ob.SaveXXYSetPos(get_x_pos, get_y_pos)
        setting.tictactoe_ob.WinDetermination(setting.win_conn_num)

        x_xy_set_list = setting.tictactoe_ob.GetXXYSetPos()
        PrintSettingList(x_xy_set_list, "x_xy_set_list")

def MiddleMouseCallBack(event):
    setting.window_canvas.delete("all")
    setting.tictactoe_ob.PrintBoard()
    setting.tictactoe_ob.DeleteXYList()


def PrintSettingList(input_list, list_name):
    input_list_size = len(input_list)

    if(input_list_size == 0):
        print("{x} is empty!".format(x = list_name))
    elif(input_list_size == 1):
        print("{y} = [{x}]".format(x = input_list[0], y = list_name))
    else:
        for x in range(input_list_size):
            if(x == 0):
                print("{y} = [{x}".format(x = input_list[x], y = list_name), end = "")
            elif(x == input_list_size-1):
                print(", {x}]".format(x = input_list[x]))
            else:
                print(", {x}".format(x = input_list[x]), end = "")
