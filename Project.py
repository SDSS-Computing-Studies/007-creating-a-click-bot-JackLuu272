import pyautogui as py
import time

class cord():
    replay = (674,477)
    dino = (430,483)
    # box 449,512

def reset():
    py.click(cord.replay)
    print("The game will be replayed.")

#def spce():
    #py.keyDown('space')
    #time.sleep(0.1)
    #py.keyUp('space')
    #time.sleep(0.1)

#def dodge():
    #py.keyDown('down')
    #time.sleep(0.1)
    #py.keyUp('down')
    #time.sleep(0.1)

def dinosa(): 
    cactus1st = py.locateCenterOnScreen('cactus1.png', grayscale=True, region = (450,480,25,38))
    if cactus1st is not None:
        py.moveTo(cactus1st)
        print(cactus1st)
        py.press('space')
        time.sleep(0.1)
       
def dinosb():
    cactus2nd = py.locateCenterOnScreen('cactus2.png', grayscale=True, region = (450,480,25,38))
    if cactus2nd is not None:
        py.moveTo(cactus2nd)
        print(cactus2nd)
        py.press('space')
        time.sleep(0.1)
        
def dinosc():
    cactus3rd = py.locateCenterOnScreen('cactus3.png', grayscale=True, region = (450,480,25,38))
    if cactus3rd is not None:
        py.moveTo(cactus3rd)
        print(cactus3rd)
        py.press('space')
        time.sleep(0.1)

def pter():
    supercreep = py.locateCenterOnScreen('scarymonster.png', grayscale=True, region = (450,480,25,38))
    if supercreep is not None:
        py.moveTo(supercreep)
        print(supercreep)
        py.press('down')
        time.sleep(0.1)
        
time.sleep(3)
reset()    

while True:
    dinosa()
    dinosb()
    dinosc()
    pter()
    
                                    