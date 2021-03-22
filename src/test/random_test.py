# group = [[571.0, 807.5], [571.0, 770.0], [571.0, 732.5], [571.0, 695.5], [571.0, 657.5], [571.0, 620.5], [571.0, 583.0], [571.0, 545.5], [571.0, 508.5]]
group = [[1,1], [1,2], [1,3], [1,4], [1,5], [1,6], [1,7], [1,8], [1,9]]
group_val = 3

possible_moves = []

flattened_y = [[1,6]]

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

print(possible_moves)