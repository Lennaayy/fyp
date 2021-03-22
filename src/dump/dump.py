import random 
import logic.legal_moves as lg
import logic.possible_moves as pm

# all_block_coords = [[1, 1], [1, 2], [1, 3], [1, 4], [2, 2], [2, 3], [2, 4], [2, 5], [3, 3], [3, 4], [3, 5], [3, 6]]
all_block_coords = [[652.5, 620.5], [652.5, 583.0], [615.5, 583.0], [652.5, 545.5], [615.5, 545.5], [578.0, 545.5], [652.5, 508.0], [615.5, 508.0], [578.0, 508.0], [615.5, 470.5], [578.0, 470.5], [578.0, 433.5]]
blocks_left = all_block_coords
group_val = 2
all_legal_block_groupings = lg.legal_moves(all_block_coords, group_val)
all_possible_block_groupings = pm.possible_moves(all_block_coords, group_val)

doing_level = True

while doing_level:

    # Find the legal moves
    legal_block_groupings = lg.legal_moves(blocks_left, group_val)
    
    # If none exist, reset the level as it is unsolveable
    if not legal_block_groupings:
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

    print(grouping)

    # Remove the blocks of the grouping from the blocks remaining list
    blocks_left = [block for block in blocks_left if block not in grouping]

    # If no blocks remaining the level is solves and the next one will start
    if(len(blocks_left) == 0):
        doing_level = False

print("Done level")

