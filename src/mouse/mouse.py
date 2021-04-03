import readers.coord_read as cr
import pyautogui as pg

def reset():
    # The bounding box coordinates of the game 
    tlx, tly, brx, bry = cr.window_coords()

    # The position of the reset button
    reset_x, reset_y = cr.reset_coords(tlx, tly, brx, bry)

    # Click the reset button
    pg.leftClick(reset_x, reset_y)
    pg.mouseDown()
    pg.mouseUp()

def remove_group(grouping):
    # Click on the first block and release on the last one (index -1 from end)
    pg.moveTo(grouping[0][0], grouping[0][1])
    pg.mouseDown(button='left')
    pg.moveTo(grouping[-1][0], grouping[-1][1])
    pg.mouseUp()