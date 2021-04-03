import collections


from collections import Counter

def min_distance(grouping, same_x, blocks_left, group_val):

    # Flatten out the blocks
    all_x = [block[0] for block in blocks_left]
    all_y = [block[1] for block in blocks_left]

    # Count how many blocks in each row and column
    x_ctr = Counter(all_x)
    y_ctr = Counter(all_y)

    x_keys = []
    y_keys = []

    min_x_dict = {}
    max_x_dict = {}
    min_y_dict = {}
    max_y_dict = {}

    # Find all groups of blocks that are exactly the group value amount of blocks in that row/column
    for key in x_ctr:
        if x_ctr[key] == group_val+1:
            x_keys.append(key)
    
    for key in y_ctr:
        if y_ctr[key] == group_val+1:
            y_keys.append(key) 

    # Loop through all block remaining
    for block in blocks_left:
        if block[0] in x_keys:
            key = block[0]

            # Create a dictionary of the minimum corresponding y value for groupings in x that are of val group_val
            if block[0] not in min_x_dict:
                min_x_dict[key] = block[1]
            else: 
                if min_x_dict[key] > block[1]:
                    min_x_dict[key] = block[1]
            
            # Create a dictionary of the maximum corresponding y value for groupings in x that are of val group_val
            if block[0] not in max_x_dict:
                max_x_dict[key] = block[1]
            else: 
                if max_x_dict[key] < block[1]:
                    max_x_dict[key] = block[1]
        
        if block[1] in y_keys:
            key = block[1]

            # Create a dictionary of the minimum corresponding x value for groupings in y that are of val group_val
            if block[1] not in min_y_dict:
                min_y_dict[key] = block[0]
            else: 
                if min_y_dict[key] > block[0]:
                    min_y_dict[key] = block[0]
            
            # Create a dictionary of the maximum corresponding x value for groupings in y that are of val group_val
            if block[1] not in max_y_dict:
                max_y_dict[key] = block[0]
            else: 
                if max_y_dict[key] < block[0]:
                    max_y_dict[key] = block[0]
    
    min_distance = 10000

    for key in x_keys:
        if abs(max_x_dict[key] - min_x_dict[key]) < min_distance:
            min_distance = max_x_dict[key] - min_x_dict[key]
    
    for key in y_keys:
        if abs(max_y_dict[key] - min_y_dict[key]) < min_distance:
            min_distance = max_y_dict[key] - min_y_dict[key]

    if same_x:
        if abs(grouping[0][1] - grouping[-1][1]) == min_distance:
            return True
        else:
            return False
    else:
        if abs(grouping[0][0] - grouping[-1][0]) == min_distance:
            return True
        else:
            return False
