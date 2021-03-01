import readers.coord_read as cr
import readers.block_read as br
import readers.img_read as ir
import pyautogui as pg
from PIL import ImageGrab
import random
import time
import keyboard

def check_valid(list, index, gap):
    return (index+gap) <= len(list)-1, (index-gap) >= 0

# Get the required grouping value 
group_val = br.group_requirement_value("game_state.png")

# Get all blocks on screen
blockCoords = br.find_blocks("game_state.png", 0, 0)

print("Grouping Requirement: ", group_val)

print("All Blocks: ", blockCoords)

pair_list = []
for i in range(len(blockCoords)):

    print("Current Block: ", blockCoords[i])
    same_x = []
    same_y = []

    for block in blockCoords[i:]:
        print("Block Comparison:", block)
        if(blockCoords[i][0] == block[0]):
            same_x.append(block[1])
        if(blockCoords[i][1] == block[1]):
            same_y.append(block[0])

    same_x.sort()
    same_y.sort()

    y_index = same_x.index(blockCoords[i][1])
    x_index = same_y.index(blockCoords[i][0])

    print("Same X: ", same_x)
    print("Same Y: ", same_y)

    above_x, below_x = check_valid(same_x, y_index, group_val)
    above_y, below_y = check_valid(same_y, x_index, group_val)

    print("Above X: ", above_x, "Below X: ", below_x)
    print("Above Y: ", above_y, "Below Y: ", below_y)
    
    if(above_x):
        pair_list.append([[blockCoords[i][0], blockCoords[i][1]], [blockCoords[i][0], same_x[y_index+group_val]]])
    if(below_x):
        pair_list.append([[blockCoords[i][0], blockCoords[i][1]], [blockCoords[i][0], same_x[y_index-group_val]]])
    if(above_y):
        pair_list.append([[blockCoords[i][0], blockCoords[i][1]], [same_y[x_index+group_val], blockCoords[i][1]]])
    if(below_y):
        pair_list.append([[blockCoords[i][0], blockCoords[i][1]], [same_y[x_index-group_val], blockCoords[i][1]]])

print("Final Pairs: ",pair_list)

# Select two random blocks
r = random.choice(pair_list)

print(r)







