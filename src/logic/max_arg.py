# Returns the index of the maximum Q-Table value for exploitation 
def max_argument(q_table, all_possible_block_groupings, legal_block_groupings):
    indexes = [] 

    # Get all legal indexes
    for i in range(len(all_possible_block_groupings)): 
        if (legal_block_groupings.count(all_possible_block_groupings[i]) > 0): 
            indexes.append(i) 

    max, action = -1000, 0

    # Find the maximum value's index
    for i in indexes:
        if q_table[0][i] > max:
            action = i
            max = q_table[0][i]
    
    return action

# Returns the maximum Q-Table value for learning purposes 
def max_q_value(q_table, all_possible_block_groupings, legal_block_groupings):
    indexes = [] 

    # Get all the legal states
    for i in range(len(all_possible_block_groupings)): 
        if (legal_block_groupings.count(all_possible_block_groupings[i]) > 0): 
            indexes.append(i) 

    max = -1000

    # Find the maximum value
    for i in indexes:
        if q_table[0][i] > max:
            max = q_table[0][i]
    
    return max