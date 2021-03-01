import cv2 
import pyautogui as pg

print(pg.position())

def edge_detect(file_name):
    image = cv2.imread(file_name)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    cnts = cv2.findContours(gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]

    image_number = 0
    for c in cnts:
        area = cv2.contourArea(c)
        if area == 361.0 or area == 527.0:
            x,y,w,h = cv2.boundingRect(c)
            print("X:{} Y:{} W:{} H:{}", x,y,w,h)
            cv2.rectangle(image, (x, y), (x + w, y + h), (36,255,12), 2)
            image_number += 1
        cv2.imwrite('cnt_'+file_name, image)
