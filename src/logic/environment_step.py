import logic.calculate_reward as cr

def environment_step(all_possible_block_groupings, state, action, blocks_left, all_block_coords, group_val, printBool, level):
    grouping = all_possible_block_groupings[action]

    if printBool:
        print("Action Taken:", grouping)

    # Variable for crossing on the x or y axis
    same_x = (grouping[0][0] == grouping[-1][0])

    # Find the coordinates of the outer blocks
    xmin = min(grouping[0][0], grouping[-1][0])
    xmax = max(grouping[0][0], grouping[-1][0])
    ymin = min(grouping[0][1], grouping[-1][1])
    ymax = max(grouping[0][1], grouping[-1][1])
    new_blocks_left = []

    # Remove all blocks between the outer blocks
    for block in blocks_left:
        if not(xmin <= block[0] <= xmax and ymin <= block[1] <= ymax):
            new_blocks_left.append(block)

    # if printBool:
    #     print("BLOCKS LEFT:", new_blocks_left)


    reward, doing_level, new_blocks_left = cr.calculate_reward(grouping, blocks_left, new_blocks_left, all_block_coords, group_val, same_x, level)

    if printBool:
        print("Reward:", reward)
    # Move to the next stae
    next_state = state

    return next_state, reward, doing_level, new_blocks_left

