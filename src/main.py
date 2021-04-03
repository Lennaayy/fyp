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
gamma = 0.2
epsilon = 0.4
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

        # Grab the game state, this is only needed once per level as we can return to the starting state if a reset is needed
        img = ImageGrab.grab(bbox=(tlx, tly, brx, bry))
        img.save("game_state.png", "PNG")

        # Get the required grouping value and level
        group_val = br.group_requirement_value(tlx, tly, brx, bry)
        level = br.get_level(tlx, tly, brx, bry)

        # Get all blocks on screen
        all_block_coords = br.find_blocks("game_state.png", tlx, tly)
        all_possible_block_groupings = pm.possible_moves(all_block_coords, group_val)
        blocks_left = all_block_coords

        # Find the legal moves
        legal_block_groupings = lg.legal_moves(blocks_left, group_val)

        action_space = len(all_possible_block_groupings)
        q_table = np.zeros([observation_space, action_space])
        groups = []

        # Reset all Parameters
        print(f"\nLevel {level} Started :)")
        print(f"All Blocks Coords {all_block_coords}\n")
        epochs = 1
        alpha = 0.6
        alpha_copy = 0.6
        gamma = 0.6
        epsilon = 0.4
        epsilon_copy = 0.4
        move_count = 0
        max_moves = 0
        printBool = False

        # Start the Level until it is solved
        doing_level = True
        while doing_level:
            if keyboard.is_pressed('q'):  # if key 'q' is pressed/held the program will quit
                break

            if epochs % 500 == 0:
                print("On Epochs:", epochs)
                epsilon_copy *= 0.99
                # alpha_copy *= 0.95

            if move_count < (epochs//1500):
                epsilon = 0.01
                alpha = 1
            else: 
                epsilon = epsilon_copy
                alpha = alpha_copy

            move_count += 1

            if move_count > max_moves:
                max_moves = move_count
            
            if random.uniform(0, 1) < epsilon:
                move = random.choice(legal_block_groupings)
                action = all_possible_block_groupings.index(move) # Explore action space
            else:
                action = ma.max_argument(q_table, all_possible_block_groupings, legal_block_groupings) # Exploit learned values

            # Take the action in the environment while retrieving the information
            next_state, reward, doing_level, blocks_left = es.environment_step(all_possible_block_groupings, state, action, blocks_left, all_block_coords, group_val, printBool, level)
            groups.append(all_possible_block_groupings[action])

            # Find the legal moves
            legal_block_groupings = lg.legal_moves(blocks_left, group_val)

            old_value = q_table[state, action]
            next_max = ma.max_q_value(q_table, all_possible_block_groupings, legal_block_groupings, printBool)
            
            new_value = (1 - alpha) * old_value + alpha * (reward + gamma * next_max)
            q_table[state, action] = new_value

            if reward == -20:
                groups = []
                move_count = 0

            if doing_level == False:
                print("Solved on epoch:", epochs)
                cl.complete_level(groups)

            state = next_state
            epochs += 1

            if max_moves < (epochs // 1500)+1:
                q_table = np.zeros([observation_space, action_space])
                groups = []
                move_count = 0
                max_moves = 0
                epochs = 0
                epsilon = 0.4
                # print("moves:", move_count)
                # printBool = True
                # time.sleep(1.5)




except KeyboardInterrupt:
    pass
