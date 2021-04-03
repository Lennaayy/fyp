from numpy.core.shape_base import block
import logic.reset_condition as rc
from collections import Counter

def calculate_reward(grouping, blocks_left, new_blocks_left, all_block_coords, group_val, same_x, level):
    edge_cases1 = ["27", "41", "44", "50"]
    edge_cases2 = ["27", "34"]

    # If no blocks remaining the level is solved and the next one will start
    if(len(new_blocks_left) == 0):
        doing_level = False
        reward = 1000
    else:
        doing_level = True

    # Find if the game needs to be reset
    reset_condition = rc.reset(new_blocks_left, group_val, doing_level)

    # Low score on reset, bad move and restart board
    if(reset_condition):
        new_blocks_left = all_block_coords
        reward = -20

    elif (same_x): 
        all_x = [block[0] for block in new_blocks_left]

        if (grouping[0][0]) not in all_x:
            if level == "34":
                reward = 10
            if level in edge_cases1 and abs(grouping[0][1] - grouping[-1][1]) <= (group_val+1)*38:
                reward = -1
            else: 
                reward = 100
        elif depletable_row_present(blocks_left, group_val):
            if level in edge_cases2:
                reward = 1
            else:
                reward = -10
        else: 
            if level == "39":
                reward = row_count(blocks_left, grouping, same_x)
            else:
                reward = 1

    else: 
        all_y = [block[1] for block in new_blocks_left]

        if (grouping[0][1]) not in all_y:
            if level == "34":
                reward = 10
            elif level in edge_cases1 and abs(grouping[0][0] - grouping[-1][0]) <= (group_val+1)*38:
                reward = -1
            else:
                reward = 100
        elif depletable_row_present(blocks_left, group_val):
            if level in edge_cases2:
                reward = 1
            else:
                reward = -10
        else: 
            if level == "39":
                reward = row_count(blocks_left, grouping, same_x)
            else:
                reward = 1

    return reward, doing_level, new_blocks_left


def depletable_row_present(blocks_left, group_val):
    # Flatten out the blocks
    all_x = [block[0] for block in blocks_left]
    all_y = [block[1] for block in blocks_left]

    # Count how many blocks in each row and column
    x_ctr = Counter(all_x)
    y_ctr = Counter(all_y)

    for key in x_ctr:
        if x_ctr[key] == group_val+1:
            return True
    
    for key in y_ctr:
        if y_ctr[key] == group_val+1:
            return True

    return False

def row_count(blocks_left, grouping, same_x):
    all_x = [block[0] for block in blocks_left]
    all_y = [block[1] for block in blocks_left]

    x_ctr = Counter(all_x)
    y_ctr = Counter(all_y)

    if(same_x):
        if(x_ctr[grouping[0][1]] == 6):
            return 10
        else: 
            return -10
    else:
        if(y_ctr[grouping[0][0]] == 6):
            return 10
        else: 
            return -10