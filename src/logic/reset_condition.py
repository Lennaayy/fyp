from numpy.core.shape_base import block
import logic.legal_moves as lg
import mouse.mouse as mouse

def reset(blocks_left, group_val, doing_level):
    # Find the legal moves
    legal_block_groupings = lg.legal_moves(blocks_left, group_val)
    
    # If none exist and the level isn't complete, reset the level as it is unsolveable
    if not legal_block_groupings and doing_level:
        # mouse.reset()
        return True
    
    return False