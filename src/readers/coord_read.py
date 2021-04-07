from win32gui import FindWindow, GetWindowRect
import pygetwindow
import win32gui

# Find the coordinates of the window
def window_coords():

    # Get the window
    win = pygetwindow.getWindowsWithTitle("Adobe Flash Player 32")[0]

    # Resize
    win.size = (800, 600)

    # Get the window's coordinates
    window_handle = FindWindow(None, "Adobe Flash Player 32")

    # Set to the foreground
    win32gui.SetForegroundWindow(window_handle)

    rect = GetWindowRect(window_handle)
    tlx = rect[0]
    tly = rect[1]
    brx = rect[2]
    bry = rect[3]

    return tlx, tly, brx, bry

# Find the reset button's coordinates 
def reset_coords(tlx, tly, brx, bry):

    # Use proportions to get the coordinates 
    reset_x = ((brx-tlx)*0.075)+tlx
    reset_y = ((bry-tly)*0.9)+tly
    
    return reset_x, reset_y
