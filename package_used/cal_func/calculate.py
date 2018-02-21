#! /usr/bin/env python3.6

def CalPrintCirclePt(mouse_x, mouse_y, x_list, y_list):
    final_x0 = 0
    final_y0 = 0
    final_x1 = 0
    final_y1 = 0
    shrink_down_ratio = 0.1
    x_grid_length = x_list[1] - x_list[0]
    y_grid_length = y_list[1] - y_list[0]
    x_shrink_down_length = shrink_down_ratio * x_grid_length
    y_shrink_down_length = shrink_down_ratio * y_grid_length

    get_x_pos = 0
    get_y_pos = 0

    get_x_pos = CalApproxPosition(mouse_x, x_list)
    get_y_pos = CalApproxPosition(mouse_y, y_list)

    final_x0 = x_list[get_x_pos] + x_shrink_down_length
    final_y0 = y_list[get_y_pos] + y_shrink_down_length
    final_x1 = x_list[get_x_pos+1] - x_shrink_down_length
    final_y1 = y_list[get_y_pos+1] - y_shrink_down_length

    return(final_x0, final_y0, final_x1, final_y1, get_x_pos, get_y_pos)


def CalApproxPosition(mouse_pos, pos_list):
    get_pos = 0
    for pos in pos_list:
        if(pos > mouse_pos):
            get_pos -= 1
            break
        else:
            get_pos += 1
    return(get_pos)


def CalPrintXPt(mouse_x, mouse_y, x_list, y_list):
    final_lx0 = 0
    final_ly0 = 0
    final_lx1 = 0
    final_ly1 = 0

    final_rx0 = 0
    final_ry0 = 0
    final_rx1 = 0
    final_ry1 = 0

    shrink_down_ratio = 0.1
    x_grid_length = x_list[1] - x_list[0]
    y_grid_length = y_list[1] - y_list[0]
    x_shrink_down_length = shrink_down_ratio * x_grid_length
    y_shrink_down_length = shrink_down_ratio * y_grid_length

    get_x_pos = 0
    get_y_pos = 0

    get_x_pos = CalApproxPosition(mouse_x, x_list)
    get_y_pos = CalApproxPosition(mouse_y, y_list)

    final_lx0 = x_list[get_x_pos] + x_shrink_down_length
    final_ly0 = y_list[get_y_pos] + y_shrink_down_length
    final_lx1 = x_list[get_x_pos+1] - x_shrink_down_length
    final_ly1 = y_list[get_y_pos+1] - y_shrink_down_length

    final_rx0 = x_list[get_x_pos+1] - x_shrink_down_length
    final_ry0 = y_list[get_y_pos] + y_shrink_down_length
    final_rx1 = x_list[get_x_pos] + x_shrink_down_length
    final_ry1 = y_list[get_y_pos+1] - y_shrink_down_length

    return(final_lx0, final_ly0, final_lx1, final_ly1, final_rx0, final_ry0, final_rx1, final_ry1, get_x_pos, get_y_pos)
