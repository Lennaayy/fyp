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
            possible_count, extra, j = 0, 0, 1
            while possible_count < group_val and j < len(group):
                if group[j] in flattened_y:
                    extra+=1
                    j+=1
                else:
                    possible_count+=1
                    j+=1
            possible_moves.append([group[i], group[i+group_val]])
            for j in range(1, extra+1):
                if i+group_val+j < len(group):
                    possible_moves.append([group[i], group[i+group_val+j]])
    
    for group in groupable_y:
        for i in range(len(group)-group_val):
            possible_count, extra, j = 0, 0, 1
            while possible_count < group_val and j < len(group):
                if group[j] in flattened_x:
                    extra+=1
                    j+=1
                else:
                    possible_count+=1
                    j+=1
            possible_moves.append([group[i], group[i+group_val]])
            for j in range(1, extra+1):
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

# all_block_coords = [[652.5, 620.5], [652.5, 583.0], [615.5, 583.0], [652.5, 545.5], [615.5, 545.5], [578.0, 545.5], [652.5, 508.0], [615.5, 508.0], [578.0, 508.0], [615.5, 470.5], [578.0, 470.5], [578.0, 433.5]]
all_block_coords = [[1, 1], [1, 2], [1, 3], [1, 4], [2, 2], [2, 3], [2, 4], [2, 5], [3, 3], [3, 4], [3, 5], [3, 6]]
blocks_left = all_block_coords
group_val = 2

groupable_x, groupable_y = groupable_x_and_y(all_block_coords, group_val)

print("X:", groupable_x)
print("Y:", groupable_y)

print(possible_moves(all_block_coords, group_val))

