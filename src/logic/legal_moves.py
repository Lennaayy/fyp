def check_valid(list, index, gap):
    return (index+gap) <= len(list)-1, (index-gap) >= 0

def legal_moves(block_coords, group_val):
    legal_move_groupings = []
    for i in range(len(block_coords)):

        same_x = []
        same_y = []

        for block in block_coords[i:]:
            if(block_coords[i][0] == block[0]):
                same_x.append(block[1])
            if(block_coords[i][1] == block[1]):
                same_y.append(block[0])

        same_x.sort()
        same_y.sort()

        y_index = same_x.index(block_coords[i][1])
        x_index = same_y.index(block_coords[i][0])

        above_x, below_x = check_valid(same_x, y_index, group_val)
        above_y, below_y = check_valid(same_y, x_index, group_val)
        
        if(above_x):
            grouping = [[block_coords[i][0], block_coords[i][1]]]
            for j in range(1, group_val+1):
                grouping.append([block_coords[i][0], same_x[y_index+j]])
            legal_move_groupings.append(grouping)

        if(below_x):
            grouping = [[block_coords[i][0], block_coords[i][1]]]
            for j in range(1, group_val+1):
                grouping.append([block_coords[i][0], same_x[y_index-j]])
            legal_move_groupings.append(grouping)

        if(above_y):
            grouping = [[block_coords[i][0], block_coords[i][1]]]
            for j in range(1, group_val+1):
                grouping.append([same_y[x_index+j], block_coords[i][1]])
            legal_move_groupings.append(grouping)

        if(below_y):
            grouping = [[block_coords[i][0], block_coords[i][1]]]
            for j in range(1, group_val+1):
                grouping.append([same_y[x_index-j], block_coords[i][1]])
            legal_move_groupings.append(grouping)

    if(all_blocks_groupable(block_coords, legal_move_groupings)):
        end_blocks = []
        for group in legal_move_groupings:
            end_blocks.append([group[0], group[-1]])
        return end_blocks
    else: 
        return []

def all_blocks_groupable(block_coords, legal_move_groupings):
    block_present = False 
    for block in block_coords:
        block_present = False
        for grouping in legal_move_groupings:
            for item in grouping:
                if item == block:
                    block_present = True
                if block_present == True:
                    continue
            if block_present == True:
                continue
        if block_present == False:
            return False

    return True