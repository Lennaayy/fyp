# Check if the block has a pairing the gap amount above or below it, returning a boolean for each
def check_valid(list, index, gap):
    return (index+gap) <= len(list)-1, (index-gap) >= 0

# Find all the legal moves of the current board
def legal_moves(block_coords, group_val):
    legal_move_groupings = []

    # Loop through every block
    for i in range(len(block_coords)):

        same_x = []
        same_y = []

        # Find all blocks in the same row and column
        for block in block_coords[i:]:
            if(block_coords[i][0] == block[0]):
                same_x.append(block[1])
            if(block_coords[i][1] == block[1]):
                same_y.append(block[0])

        same_x.sort()
        same_y.sort()

        # Get the index of the current block
        y_index = same_x.index(block_coords[i][1])
        x_index = same_y.index(block_coords[i][0])

        # Check if a pairing is available in each direction
        above_x, below_x = check_valid(same_x, y_index, group_val)
        above_y, below_y = check_valid(same_y, x_index, group_val)
        
        # Add pairing if true to legal moves
        if(above_x):
            grouping = [[block_coords[i][0], block_coords[i][1]]]
            for j in range(1, group_val+1):
                grouping.append([block_coords[i][0], same_x[y_index+j]])
            legal_move_groupings.append(grouping)

        # Add pairing if true to legal moves
        if(below_x):
            grouping = [[block_coords[i][0], block_coords[i][1]]]
            for j in range(1, group_val+1):
                grouping.append([block_coords[i][0], same_x[y_index-j]])
            legal_move_groupings.append(grouping)

        # Add pairing if true to legal moves
        if(above_y):
            grouping = [[block_coords[i][0], block_coords[i][1]]]
            for j in range(1, group_val+1):
                grouping.append([same_y[x_index+j], block_coords[i][1]])
            legal_move_groupings.append(grouping)

        # Add pairing if true to legal moves
        if(below_y):
            grouping = [[block_coords[i][0], block_coords[i][1]]]
            for j in range(1, group_val+1):
                grouping.append([same_y[x_index-j], block_coords[i][1]])
            legal_move_groupings.append(grouping)

    # Check if the puzzle is still solvable, else return no legal moves causing a reset
    if(all_blocks_groupable(block_coords, legal_move_groupings)):
        end_blocks = []
        for group in legal_move_groupings:
            end_blocks.append([group[0], group[-1]])
        return end_blocks
    else: 
        return []

# Method to test every block is capable of being crossed out at least once
def all_blocks_groupable(block_coords, legal_move_groupings):

    # Loop through every block
    block_present = False 
    for block in block_coords:
        block_present = False
        # Loop through every grouping of blocks 
        for grouping in legal_move_groupings:
            # Check block is present in at least one grouping
            for item in grouping:
                if item == block:
                    block_present = True
                if block_present == True:
                    continue
            if block_present == True:
                continue
        # If any block not crossable, return false as all block aren't groupable, causing a reset
        if block_present == False:
            return False

    return True