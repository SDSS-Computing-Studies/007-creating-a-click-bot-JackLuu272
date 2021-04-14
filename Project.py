import pyautogui
import time
from PIL import ImageGrab
from PIL import ImageOps
from numpy import *

class cord():
    replay = (674,477)
    dino = (430,483)
    # box 449,512

def reset():
    pyautogui.click(cord.replay)
    print("The game will be replayed.")

def spce():
    pyautogui.keyDown('space')
    time.sleep(0.1)
    pyautogui.keyUp('space')
    time.sleep(0.1)

def dinosa(): 
    fossil = (cord.dino[0]+ 19, cord.dino[1], cord.dino[1]+ 3, cord.dino[0]+29)
    sample = ImageGrab.grab(fossil)
    detect = ImageOps.grayscale(sample)
    a = array(detect.getcolors())
    print(a.sum())         

time.sleep(4.5)
reset()    

while True:
    dinosa()
    #if (dinosa() != ):
        #spce()
        #time.sleep(0.001)

                                    