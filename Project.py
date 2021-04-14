import pyautogui as py
import time

class cord():
    replay = (674,477)
    dino = (430,483)
    # box 449,512

def reset():
    py.click(cord.replay)
    print("The game will be restarted.")

def dinosa():
    cactus1st = py.locateCenterOnScreen('cactus1.png', grayscale=True, region = (450,480,110,100))
    if cactus1st is not None:
        py.moveTo(cactus1st)
        print(cactus1st)
        py.press('space')
    
def dinosb():
    cactus2nd = py.locateCenterOnScreen('cactus2.png', grayscale=True, region = (450,480,110,100))
    if cactus2nd is not None:
        py.moveTo(cactus2nd)
        print(cactus2nd)
        py.press('space')
        
def dinosc():
    cactus3rd = py.locateCenterOnScreen('cactus3.png', grayscale=True, region = (450,480,110,100))
    if cactus3rd is not None:
        py.moveTo(cactus3rd)
        print(cactus3rd)
        py.press('space')

def dinosd():
    cactus4th = py.locateCenterOnScreen('cactus4.png', grayscale=True, region = (450,480,110,100))
    if cactus4th is not None:
        py.moveTo(cactus4th)
        print(cactus4th)
        py.press('space')

def pter():
    supercreep = py.locateCenterOnScreen('scarymonster.png', grayscale=True, region = (450,480,110,100))
    if supercreep is not None:
        py.moveTo(supercreep)
        print(supercreep)
        py.press('down')

def over():
    restart = py.locateCenterOnScreen('end.png')
    if restart is not None:
        py.click(cord.replay)

time.sleep(3)

def main():
    reset()    
    while True:
        dinosa()
        dinosb()
        dinosc()
        dinosd()
        pter()
        over()
        
main()
                                    