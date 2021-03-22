import random 
import logic.legal_moves as lg
import logic.possible_moves as pm
import logic.max_arg as ma
import logic.environment_step as es
import logic.complete_level as cl
import numpy as np
import keyboard

# Hyperparameters
alpha = 0.1
gamma = 0.6
epsilon = 0.2
observation_space = 1
state = 0

all_block_coords = [[1,1], [1,2], [1,3], [1,4], [2,1], [2,4], [3,2], [3,3], [4,1], [4,2], [4,3], [4,4], [6,1], [5,2], [5,3], [6,4],[7,1], [7,3], [8,1], [8,2], [8,3], [8,4], [9,1], [9,2] ,[9,3], [9,4], [10,2], [10,4]]
# all_block_coords = [[1,3], [2,1], [2,2], [2,3], [3,1], [3,2], [3,3], [3,4], [4,1], [4,2], [4,3], [5,3]]
# all_block_coords = [[1, 1], [1, 2], [1, 3], [1, 4], [2, 2], [2, 3], [2, 4], [2, 5], [3, 3], [3, 4], [3, 5], [3, 6]]
# all_block_coords = [[652.5, 620.5], [652.5, 583.0], [615.5, 583.0], [652.5, 545.5], [615.5, 545.5], [578.0, 545.5], [652.5, 508.0], [615.5, 508.0], [578.0, 508.0], [615.5, 470.5], [578.0, 470.5], [578.0, 433.5]]
blocks_left = all_block_coords
group_val = 3
all_legal_block_groupings = lg.legal_moves(all_block_coords, group_val)
all_possible_block_groupings = pm.possible_moves(all_block_coords, group_val)


action_space = len(all_possible_block_groupings)
q_table = np.zeros([observation_space, action_space])

doing_level = True

while doing_level:

    if keyboard.is_pressed('q'):  # if key 'q' is pressed/held the program will quit
        break

    # Find the legal moves
    legal_block_groupings = lg.legal_moves(blocks_left, group_val)

    print("All:", all_possible_block_groupings)
    print("Legal:", legal_block_groupings)
    print("Left:", blocks_left)
    print("Table Values:", q_table[0])
    
    if random.uniform(0, 1) < epsilon:
        move = random.choice(legal_block_groupings)
        action = all_possible_block_groupings.index(move) # Explore action space
    else:
        action = ma.max_argument(q_table, all_possible_block_groupings, legal_block_groupings) # Exploit learned values

    print("Action:", action)

    # Take the action in the environment while retrieving the information
    next_state, reward, doing_level, blocks_left = es.environment_step(all_possible_block_groupings, action, blocks_left, all_block_coords, group_val)

    old_value = q_table[state, action]
    next_max = np.max(q_table[next_state])
    
    new_value = (1 - alpha) * old_value + alpha * (reward + gamma * next_max)
    q_table[state, action] = new_value

    # After sufficient learning, complete the level with the learned q_values
    if doing_level == False:
        # cl.complete_level(q_table, all_block_coords, group_val)
        print("yay")

    state = next_state
    # epochs += 1


print("Done level")

