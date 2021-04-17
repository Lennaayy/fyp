import mouse.mouse as mouse
import keyboard

# Complete level :)
def complete_level(groups):
    for group in groups:
        
        if keyboard.is_pressed('q'):  # if key 'q' is pressed/held the program will quit
                exit()

        mouse.remove_group(group)



