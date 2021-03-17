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
        if keyboard.is_pressed('q'):  # if key 'q' is pressed/held the program will quit
            break

        # Grab the game state, this is only needed once per level as we can return to the starting state if a reset is needed
        img = ImageGrab.grab(bbox=(tlx, tly, brx, bry))
        img.save("game_state.png", "PNG")

        # Get the required grouping value 
        group_val = br.group_requirement_value(tlx, tly, brx, bry)

        # Get all blocks on screen
        all_block_coords = br.find_blocks("game_state.png", tlx, tly)
        blocks_left = all_block_coords
        print(all_block_coords)
        
        # Start the Level until it is solved
        doing_level = True
        while doing_level:
            if keyboard.is_pressed('q'):  # if key 'q' is pressed/held the program will quit
                break

            # Find the legal moves
            legal_block_groupings = lg.legal_moves(blocks_left, group_val)
            
            # If none exist, reset the level as it is unsolveable
            if not legal_block_groupings:
                pg.leftClick(reset_x, reset_y)
                pg.mouseDown()
                pg.mouseUp()
                blocks_left = all_block_coords
                continue

            # Select a random block grouping
            good_choice = False
            while not good_choice:
                grouping = random.choice(legal_block_groupings)
                blocks_left_copy = blocks_left
                blocks_left_copy = [block for block in blocks_left_copy if block not in grouping]
                next_grouping = lg.legal_moves(blocks_left_copy, group_val)

                if len(blocks_left_copy) == 0:
                    good_choice = True 
                elif not next_grouping: 
                    good_choice = False 
                else:
                    good_choice = True

            # Click on the first block and release on the last one (index -1 from end)
            pg.moveTo(grouping[0][0], grouping[0][1])
            pg.mouseDown(button='left')
            pg.moveTo(grouping[-1][0], grouping[-1][1])
            pg.mouseUp()
            # https://pyautogui.readthedocs.io/en/latest/mouse.html

            # Remove the blocks of the grouping from the blocks remaining list
            blocks_left = [block for block in blocks_left if block not in grouping]

            # If no blocks remaining the level is solves and the next one will start
            if(len(blocks_left) == 0):
                doing_level = False

except KeyboardInterrupt:
    pass
