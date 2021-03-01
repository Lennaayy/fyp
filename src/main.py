from numpy.core.shape_base import block
import readers.coord_read as cr
import readers.block_read as br
import logic.legal_moves as lg
import pyautogui as pg
from PIL import ImageGrab
import random
import time
import keyboard

# The bounding box coordinates of the game 
tlx, tly, brx, bry = cr.window_coords()
reset_x, reset_y = cr.reset_coords(tlx, tly, brx, bry)
random.seed()

try:
    while True:
        if keyboard.is_pressed('q'):  # if key 'q' is pressed/held
            break

        # Grab the game_state
        img = ImageGrab.grab(bbox=(tlx, tly, brx, bry))
        img.save("game_state.png", "PNG")

        # Get the required grouping value 
        group_val = br.group_requirement_value("game_state.png")

        # Get all blocks on screen
        all_block_coords = br.find_blocks("game_state.png", tlx, tly)
        blocks_left = all_block_coords
        

        doing_level = True

        while doing_level:
            if keyboard.is_pressed('q'):  # if key 'q' is pressed/held
                break

            # Find the legal moves
            pair_list = lg.legal_moves(blocks_left, group_val)
            
            # If none exist, reset the level as it is unsolveable
            if not pair_list:
                pg.leftClick(reset_x, reset_y)
                pg.mouseDown()
                pg.mouseUp()
                blocks_left = all_block_coords
                continue

            # Select a random block pairing
            pair = random.choice(pair_list)

            # Click on the first block and release on the second
            pg.moveTo(pair[0][0], pair[0][1])
            pg.mouseDown(button='left')
            pg.moveTo(pair[1][0], pair[1][1])
            pg.mouseUp()
            # https://pyautogui.readthedocs.io/en/latest/mouse.html

            # Remove the pair from the blocks remaining list
            blocks_left = [block for block in blocks_left if block not in pair]

            if(len(blocks_left) == 0):
                doing_level = False

except KeyboardInterrupt:
    pass
