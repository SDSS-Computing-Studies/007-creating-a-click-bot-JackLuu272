import pyautogui
import time
from PIL import ImageGrab
from PIL import ImageOps
from numpy import *

replay = (675,475)
dino = (435,495)

def reset():
    pyautogui.click(replay)
    print("The game will be replayed.")

def spce():
    time.sleep(0.1)
    pyautogui.keyDown('space')

def dinosa():
    fossil = (dino[0]+55, dino[1], dino[1]+145, dino[0]+5)
    sample = ImageGrab.grab(fossil)
    detect = ImageOps.grayscale(sample)
    iden = array(detect.getcolors())
    print(iden)

time.sleep(5)
reset()    

while True:
    dinosa()
                                               
    