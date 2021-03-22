from logic.legal_moves import all_blocks_groupable
import logic.reset_condition as rc
import mouse.mouse as mouse

def environment_step(all_possible_block_groupings, action, blocks_left, all_block_coords, group_val):
    grouping = all_possible_block_groupings[action]

    # mouse.remove_group(grouping)

    xmin = min(grouping[0][0], grouping[-1][0])
    xmax = max(grouping[0][0], grouping[-1][0])
    ymin = min(grouping[0][1], grouping[-1][1])
    ymax = max(grouping[0][1], grouping[-1][1])
    new_blocks_left = []

    for block in blocks_left:
        if not(xmin <= block[0] <= xmax and ymin <= block[1] <= ymax):
            new_blocks_left.append(block)

    # print("BLOCKS LEFT:", new_blocks_left)


    # If no blocks remaining the level is solves and the next one will start
    if(len(new_blocks_left) == 0):
        doing_level = False
        print("LEVEL DONE")
        reward = 10000000
    else:
        doing_level = True

    reset_condition = rc.reset(new_blocks_left, group_val, doing_level)

    if(reset_condition):
        reward = -100
        new_blocks_left = all_block_coords
    else: 
        reward = 1

    next_state = 0

    return next_state, reward, doing_level, new_blocks_left

