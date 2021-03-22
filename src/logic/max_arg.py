import numpy as np

def max_argument(q_table, all_possible_block_groupings, legal_block_groupings):
    indexes = [] 

    for i in range(len(all_possible_block_groupings)): 
        if (legal_block_groupings.count(all_possible_block_groupings[i]) > 0): 
            indexes.append(i) 

    max = np.max([q_table[0][i] for i in indexes])
    
    return np.where(q_table[0] == max)[0][0]