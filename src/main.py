from numpy.core.shape_base import block
import readers.coord_read as cr
import readers.block_read as br
import logic.legal_moves as lg
import logic.possible_moves as pm
import logic.environment_step as es
import logic.max_arg as ma
import logic.complete_level as cl
from PIL import ImageGrab
import random
import numpy as np
import keyboard
import time

# Hyperparameters
alpha = 0.1
gamma = 0.6
epsilon = 0.1
observation_space = 1
state = 0

# The bounding box coordinates of the game 
tlx, tly, brx, bry = cr.window_coords()
reset_x, reset_y = cr.reset_coords(tlx, tly, brx, bry)
random.seed()

try:
    while True:
        if keyboard.is_pressed('q'):  # if key 'q' is pressed/held the program will quit
            break

        time.sleep(1)

        # Grab the game state, this is only needed once per level as we can return to the starting state if a reset is needed
        img = ImageGrab.grab(bbox=(tlx, tly, brx, bry))
        img.save("game_state.png", "PNG")

        # Get the required grouping value 
        group_val = br.group_requirement_value(tlx, tly, brx, bry)

        # Get all blocks on screen
        all_block_coords = br.find_blocks("game_state.png", tlx, tly)
        all_possible_block_groupings = pm.possible_moves(all_block_coords, group_val)
        blocks_left = all_block_coords

        action_space = len(all_possible_block_groupings)
        q_table = np.zeros([observation_space, action_space])
        groups = []

        # Start the Level until it is solved
        doing_level = True
        while doing_level:
            if keyboard.is_pressed('q'):  # if key 'q' is pressed/held the program will quit
                break

            # Find the legal moves
            legal_block_groupings = lg.legal_moves(blocks_left, group_val)

            # print("All:", all_possible_block_groupings)
            # print("Legal:", legal_block_groupings)
            # print("Left:", blocks_left)
            # print("Table Values:", q_table[0])
            
            if random.uniform(0, 1) < epsilon:
                move = random.choice(legal_block_groupings)
                action = all_possible_block_groupings.index(move) # Explore action space
                # print("Action Chosen Random:", action)
            else:
                action = ma.max_argument(q_table, all_possible_block_groupings, legal_block_groupings) # Exploit learned values
                # print("Action Chosen Exploit:", action)


            # Take the action in the environment while retrieving the information
            next_state, reward, doing_level, blocks_left = es.environment_step(all_possible_block_groupings, action, blocks_left, all_block_coords, group_val)
            groups.append(all_possible_block_groupings[action])

            old_value = q_table[state, action]
            next_max = np.max(q_table[next_state])
            
            new_value = (1 - alpha) * old_value + alpha * (reward + gamma * next_max)
            q_table[state, action] = new_value

            if reward == -100:
                groups = []

            if doing_level == False:
                cl.complete_level(groups)

            state = next_state
            # epochs += 1

except KeyboardInterrupt:
    pass
