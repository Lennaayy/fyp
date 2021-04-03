import mouse.mouse as mouse

def complete_level(groups):

    print("Groupings to complete:", groups)

    for group in groups:
        mouse.remove_group(group)



