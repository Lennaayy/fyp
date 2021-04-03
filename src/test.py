import random 
import logic.legal_moves as lg
import logic.possible_moves as pm
import logic.max_arg as ma
import logic.environment_step as es
import logic.complete_level as cl
import numpy as np
import keyboard
import time 

# Hyperparameters
alpha = 0.1
gamma = 0.6
epsilon = 0.4
observation_space = 1
state = 0

# all_block_coords = [[678.5, 683.5], [604.0, 683.5], [678.5, 646.5], [604.0, 646.5], [716.0, 609.0], [678.5, 609.0], [604.0, 609.0], [566.5, 609.0], [716.0, 571.5], [566.5, 571.5], [716.0, 534.0], [678.5, 534.0], [641.5, 534.0], [604.0, 534.0], [566.5, 534.0], [716.0, 496.5], [678.5, 496.5], [641.5, 496.5], [604.0, 496.5], [566.5, 496.5], [716.0, 459.5], [566.5, 459.5], [716.0, 422.0], [566.5, 422.0]]


all_block_coords = [[1,1], [1,2], [1,3], [1,4], [1,5], [1,6], [1,7], [1,8], [1,9], [1,10], [1,11], [1,12],
                    [2,3], [2,4], [2,5], [2,6], [2,7], [2,8], [2,10], [2,11], [2,12],
                    [3,6], [3,8], [3,9], [3,11],
                    [4,6], [4,7], [4,8], [4,9], [4,10], [4,11],
                    [5,1], [5,6], [5,7], [5,9], [5,10], [5,11],
                    [6,1], [6,2], [6,7], [6,8], [6,9], [6,10], [6,11], [6,12],
                    [7,2], [7,7], [7,8], [7,9], [7,10], [7,11], 
                    [8,6], [8,8], [8,9], [8,10], 
                    [9,1], [9,2], [9,3], [9,4], [9,5], [9,6], [9,7], [9,8], [9,10], [9,11], [9,12],
                    [10,1], [10,2], [10,3], [10,4], [10,5], [10,6], [10,7], [10,8], [10,9], [10,10], [10,11], [10,12]]

blocks_left = all_block_coords
group_val = 5
all_legal_block_groupings = lg.legal_moves(all_block_coords, group_val)
all_possible_block_groupings = pm.possible_moves(all_block_coords, group_val)


action_space = len(all_possible_block_groupings)
q_table = np.zeros([observation_space, action_space])
groups = []

doing_level = True
printBool = False
epochs = 0
epsilon_copy = 0.4
move_count = 0

while doing_level:
            if keyboard.is_pressed('q'):  # if key 'q' is pressed/held the program will quit
                break

            # Find the legal moves
            legal_block_groupings = lg.legal_moves(blocks_left, group_val)

            if epochs == 0:
                print(legal_block_groupings)


            if epochs > 15000:
                time.sleep(1.5)
                printBool = True

            if epochs % 500 == 0:
                print("Epoch:", epochs)
                epsilon_copy *= 0.99
            
            if move_count < (epochs//1500):
                epsilon = 0.01
            else: 
                epsilon = epsilon_copy
            
            if random.uniform(0, 1) < epsilon:
                move = random.choice(legal_block_groupings)
                action = all_possible_block_groupings.index(move) # Explore action space
            else:
                action = ma.max_argument(q_table, all_possible_block_groupings, legal_block_groupings) # Exploit learned values


            # Take the action in the environment while retrieving the information
            next_state, reward, doing_level, blocks_left = es.environment_step(all_possible_block_groupings, state, action, blocks_left, all_block_coords, group_val, printBool, level="44")
            groups.append(all_possible_block_groupings[action])

            old_value = q_table[state, action]
            next_max = ma.max_q_value(q_table, all_possible_block_groupings, legal_block_groupings)
            
            new_value = (1 - alpha) * old_value + alpha * (reward + gamma * next_max)
            q_table[state, action] = new_value
            
            
            state = next_state
            epochs += 1
            move_count += 1

            if reward == -200:
                groups = []
                move_count = 0

            if doing_level == False:
                print("Final grouping:", groups)

print("Done level")

