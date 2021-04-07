import pyautogui
import time
from PIL import ImageGrab
from PIL import ImageOps
from numpy import *

replay = (665,482)
dino = (435,493)

def reset():
    pyautogui.click(replay)
    print("The game will be replayed.")

def spce():
    time.sleep(0.1)
    pyautogui.keyDown('space')

def dinosa():
    fossil = (dino[0]+60, dino[1]+5, dino[1]+160, dino[0]+10)
    sample = ImageGrab.grab(fossil)
    detect = ImageOps.grayscale(sample)
    construct = array(detect.getcolors())
    print(construct)

time.sleep(5)
reset()    

while True:
    dinosa()
                                               
    