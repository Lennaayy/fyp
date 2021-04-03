import logic.calculate_reward as cr

def environment_step(all_possible_block_groupings, state, action, blocks_left, all_block_coords, group_val, level):

    # Infer the grouping from the action number chosen
    grouping = all_possible_block_groupings[action]

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

    # Get the reward for this move, if it finishes the level, and the new blocks remaining after this move
    reward, doing_level, new_blocks_left = cr.calculate_reward(grouping, blocks_left, new_blocks_left, all_block_coords, group_val, same_x, level)

    # Move to the next stae
    next_state = state

    return next_state, reward, doing_level, new_blocks_left

