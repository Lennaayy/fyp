import cv2 
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from PIL import Image

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

def group_requirement_value(file_name):
    # Read in the game state
    img = Image.open(file_name)

    # Read all the text on screen
    string = tess.image_to_string(img)

    # Return the first digit, which is the group requirement value 
    for i in string.split():
        if i.isdigit() and i != "32":
            val = int(i)-1
            break

    return val
