import numpy as np

def max_argument(q_table, all_possible_block_groupings, legal_block_groupings):
    indexes = [] 

    for i in range(len(all_possible_block_groupings)): 
        if (legal_block_groupings.count(all_possible_block_groupings[i]) > 0): 
            # print(f"Index {i} added, {all_possible_block_groupings[i]}")
            indexes.append(i) 

    max, action = -1000, 0

    for i in indexes:
        if q_table[0][i] > max:
            action = i
            max = q_table[0][i]
    
    return action

def max_q_value(q_table, all_possible_block_groupings, legal_block_groupings, printBool):
    indexes = [] 

    for i in range(len(all_possible_block_groupings)): 
        if (legal_block_groupings.count(all_possible_block_groupings[i]) > 0): 
            # print(f"Index {i} added, {all_possible_block_groupings[i]}")
            indexes.append(i) 

    max = -1000

    for i in indexes:
        if q_table[0][i] > max:
            max = q_table[0][i]
        # if printBool:
        #     print(f"{all_possible_block_groupings[i]}:{q_table[0][i]}")
    
    return max