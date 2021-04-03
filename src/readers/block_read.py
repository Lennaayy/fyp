import cv2 
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from PIL import ImageGrab
# Return the coordinates of the blocks on screen in an array
def find_blocks(file_name, tlx, tly):
    # Read in the image, grayscale and find the countours
    image = cv2.imread(file_name)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cnts = cv2.findContours(gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]

    allCoords = []
    # Loop through the countours 
    for c in cnts:
        area = cv2.contourArea(c)

        # With this window size, all squares have an area of ~900
        if area >= 875 and area <= 975:

            # Get the coordinates of the square
            x,y,w,h = cv2.boundingRect(c)

            # Get the coordinates of the square midpoints
            squareMidX = tlx + x + (w/2)
            squareMidY = tly + y + (h/2)
            squareCoords = [squareMidX, squareMidY]

            # Add to the array if not present
            if squareCoords not in allCoords:
                allCoords.append(squareCoords)
            
            cv2.rectangle(image, (x, y), (x + w, y + h), (36,255,12), 2)
        cv2.imwrite('cnt_'+file_name, image)
    
    return allCoords

def get_image_string(filename, xmin, xmax, ymin, ymax):
    # Read in the game state
    image = cv2.imread(filename)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cropped = gray[xmin:xmax, ymin:ymax]

    # cv2.imwrite("level.png", cropped)
    
    # Read all the text on screen
    return tess.image_to_string(cropped)

def group_requirement_value(tlx, tly, brx, bry):
    string = get_image_string("game_state.png", 50, 150, 625, 775)

    # Return the first digit, which is the group requirement value 
    val = 0
    while(val == 0):
        for i in string.split():
            if i.isdigit():
                val = int(i)-1
                break
        if(val == 0):
            img = ImageGrab.grab(bbox=(tlx, tly, brx, bry))
            img.save("game_state.png", "PNG")
            string = get_image_string("game_state.png", 50, 150, 625, 775)

    return val

def get_level(tlx, tly, brx, bry):
    string = get_image_string("game_state.png", 550, 600, 550, 775)

    string = string.split('/')[0]

    val = ''.join(filter(lambda i: i.isdigit(), string))

    return val



