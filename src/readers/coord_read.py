from win32gui import FindWindow, GetWindowRect
import pygetwindow

def window_coords():
    win = pygetwindow.getWindowsWithTitle("Adobe Flash Player 32")[0]
    win.size = (800, 600)
    window_handle = FindWindow(None, "Adobe Flash Player 32")
    rect = GetWindowRect(window_handle)
    tlx = rect[0]
    tly = rect[1]
    brx = rect[2]
    bry = rect[3]
    return tlx, tly, brx, bry

def reset_coords(tlx, tly, brx, bry):
    reset_x = ((brx-tlx)*0.075)+tlx
    reset_y = ((bry-tly)*0.9)+tly
    return reset_x, reset_y
