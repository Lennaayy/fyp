from collections import Counter

def possible_moves(block_coords, group_val):

    possible_moves = []

    # Get all x and y groups
    groupable_x, groupable_y = groupable_x_and_y(block_coords, group_val)
    
    # Unwrap groups into a list of all blocks on that axis
    flattened_x = [item for sublist in groupable_x for item in sublist]
    flattened_y = [item for sublist in groupable_y for item in sublist]

    for group in groupable_x:
        for i in range(len(group)-group_val):
            static, extra, j = 0, 0, i+1

            col_group_removeables = len(group[i+1:-1])//group_val+1
            extra += (group_val+1)*col_group_removeables

            while static < group_val and j < len(group):
                if group[j] in flattened_y:
                    extra+=1
                    j+=1
                else:
                    static+=1
                    j+=1
            for j in range(extra+1):
                if i+group_val+j < len(group):
                    possible_moves.append([group[i], group[i+group_val+j]])

    
    for group in groupable_y:
        for i in range(len(group)-group_val):
            static, extra, j = 0, 0, i+1

            col_group_removeables = len(group[i+1:-1])//group_val+1
            extra += (group_val+1)*col_group_removeables

            while static < group_val and j < len(group):
                if group[j] in flattened_x:
                    extra+=1
                    j+=1
                else:
                    static+=1
                    j+=1
            for j in range(extra+1):
                if i+group_val+j < len(group):
                    possible_moves.append([group[i], group[i+group_val+j]])

    return possible_moves


def groupable_x_and_y(block_coords, group_val):

    all_x = [block[0] for block in block_coords]
    all_y = [block[1] for block in block_coords]

    x_ctr = Counter(all_x)
    y_ctr = Counter(all_y)

    groupable_x = []
    groupable_y = []

    for key in x_ctr:
        group = []
        if x_ctr[key] > group_val:
            for block in block_coords:
                if block[0] == key:
                    group.append(block)
            groupable_x.append(group)

    
    for key in y_ctr:
        group = []
        if y_ctr[key] > group_val:
            for block in block_coords:
                if block[1] == key:
                    group.append(block)
            groupable_y.append(group)
    
    return groupable_x, groupable_y

