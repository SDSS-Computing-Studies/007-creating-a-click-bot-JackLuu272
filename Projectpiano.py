import pyautogui as py
import time 

def clicktiles1():
    presser1 = locateCenterOnScreen('tiles.png', grayscale = True, region=(590,572,100,100))
    if presser1 is not None:
        py.mouseDown(x=590,y=572)

def clicktitles2():
    presser2 = locateCenterOnScreen('Tiles.png', grayscale = True, region=(524,575,100,100))
    if presser2 is not None:
        py.mouseDown(x=524,y=575)
    
def clicktitles3():
    presser3 = locateCenterOnScreen('Tiles.png', grayscale = True, region=(471,590,100,100))
    if presser3 is not None:
        py.mouseDown(x=471,y=590)
    
def clicktitles4():
    presser4 = locateCenterOnScreen('Tiles.png', grayscale = True, region=(395,599,100,100))
    if presser4 is not None:
        py.mouseDown(x=395,y=599)


    