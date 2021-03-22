import logic.possible_moves as pm
import mouse.mouse as mouse
import numpy as np

# Hyperparameters
alpha = 0.1
gamma = 0.6
epsilon = 0.99
observation_space = 1
state = 0

def complete_level(groups):

    for group in groups:
        mouse.remove_group(group)



