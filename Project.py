import pyautogui
import time
from PIL import ImageGrab
from PIL import ImageOps
from numpy import *

class cord():
    replay = (684,402)
    dino = (126,412)
#252,414 cord box
def reset():
    pyautogui.click(cord.replay)
    print("The game will be replayed.")

def spce():
    time.sleep(0.1)
    pyautogui.keyDown('space')

def dinosa():
    fossil = (cord.dino[0]+252, cord.dino[1], cord.dino[1]+292, cord.dino[0]+2)
    sample = ImageGrab.grab(fossil)
    detect = ImageOps.grayscale(sample)
    x = array(detect.getcolors())
    print(x)

time.sleep(5)
reset()    

while True:
    dinosa()
                                               
    