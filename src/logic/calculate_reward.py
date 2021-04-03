import logic.reset_condition as rc
from collections import Counter

# Find the reward value for that particular grouping
def calculate_reward(grouping, blocks_left, new_blocks_left, all_block_coords, group_val, same_x, level):
    # Some levels follow different reward metrics 
    edge_cases1 = ["27", "41", "44", "50"]
    edge_cases2 = ["27", "34"]
    edge_cases3 = ["34"]
    edge_cases4 = ["39"]

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

    # Check if crossing on x or y axis
    elif (same_x): 
        all_x = [block[0] for block in new_blocks_left]

        # High reward for depleting a row or column fully, except edge cases
        if (grouping[0][0]) not in all_x:
            if level in edge_cases3:
                reward = 10
            if level in edge_cases1 and abs(grouping[0][1] - grouping[-1][1]) <= (group_val+1)*38:
                reward = -1
            else: 
                reward = 100

        # Low reward if choosing a row or column which doesn't deplete fully when one is available, except edge cases
        elif depletable_row_present(blocks_left, group_val):
            if level in edge_cases2:
                reward = 1
            else:
                reward = -10

        # Else standard reward, except edge cases
        else: 
            if level in edge_cases4:
                reward = row_count(blocks_left, grouping, group_val, same_x)
            else:
                reward = 1

    # Check if crossing on x or y axis
    else: 
        all_y = [block[1] for block in new_blocks_left]

        # High reward for depleting a row or column fully, except edge cases
        if (grouping[0][1]) not in all_y:
            if level in edge_cases3:
                reward = 10
            elif level in edge_cases1 and abs(grouping[0][0] - grouping[-1][0]) <= (group_val+1)*38:
                reward = -1
            else:
                reward = 100
        
        # Low reward if choosing a row or column which doesn't deplete fully when one is available, except edge cases
        elif depletable_row_present(blocks_left, group_val):
            if level in edge_cases2:
                reward = 1
            else:
                reward = -10

        # Else standard reward, except edge cases
        else: 
            if level in edge_cases4:
                reward = row_count(blocks_left, grouping, group_val, same_x)
            else:
                reward = 1

    return reward, doing_level, new_blocks_left

# Check if there is a row you can fully remove with a move this turn
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

# Edge case method for levels that require setup before row depletion
def row_count(blocks_left, grouping, group_val, same_x):
    all_x = [block[0] for block in blocks_left]
    all_y = [block[1] for block in blocks_left]

    x_ctr = Counter(all_x)
    y_ctr = Counter(all_y)

    if(same_x):
        if(x_ctr[grouping[0][0]] == group_val+1):
            return 10
        else: 
            return -10
    else:
        if(y_ctr[grouping[0][1]] == group_val+1):
            return 10
        else: 
            return -10