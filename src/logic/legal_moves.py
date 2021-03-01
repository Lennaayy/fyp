def check_valid(list, index, gap):
    return (index+gap) <= len(list)-1, (index-gap) >= 0

def legal_moves(blockCoords, group_val):
    pair_list = []
    for i in range(len(blockCoords)):

        same_x = []
        same_y = []

        for block in blockCoords[i:]:
            if(blockCoords[i][0] == block[0]):
                same_x.append(block[1])
            if(blockCoords[i][1] == block[1]):
                same_y.append(block[0])

        same_x.sort()
        same_y.sort()

        y_index = same_x.index(blockCoords[i][1])
        x_index = same_y.index(blockCoords[i][0])

        above_x, below_x = check_valid(same_x, y_index, group_val)
        above_y, below_y = check_valid(same_y, x_index, group_val)
        
        if(above_x):
            pair_list.append([[blockCoords[i][0], blockCoords[i][1]], [blockCoords[i][0], same_x[y_index+group_val]]])
        if(below_x):
            pair_list.append([[blockCoords[i][0], blockCoords[i][1]], [blockCoords[i][0], same_x[y_index-group_val]]])
        if(above_y):
            pair_list.append([[blockCoords[i][0], blockCoords[i][1]], [same_y[x_index+group_val], blockCoords[i][1]]])
        if(below_y):
            pair_list.append([[blockCoords[i][0], blockCoords[i][1]], [same_y[x_index-group_val], blockCoords[i][1]]])
    
    return pair_list