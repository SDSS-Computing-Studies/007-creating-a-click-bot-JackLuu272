import pyautogui 
from pynput.mouse import Button, Controller
import keyboard 

mouse = Controller()

def clicking(x,y):
    mouse.position=(x,y)
    mouse.click(Button.left, 1)


#X:  519 Y:  494 RGB: (235, 235, 236)
#X:  614 Y:  493 RGB: ( 59,  56,  63)
#X:  720 Y:  509 RGB: (235, 235, 236)
#X:  815 Y:  501 RGB: (235, 235, 236)

yCoord = 500

while keyboard.is_pressed("q") == False:

    try:
        if pyautogui.pixel(519,yCoord)[0] == 59:
            clicking(519,yCoord)
        elif pyautogui.pixel(614,yCoord)[0] == 59:
            clicking(614,yCoord)
        elif pyautogui.pixel(720,yCoord)[0] == 59:
            clicking(720,yCoord)
        elif pyautogui.pixel(815,yCoord)[0] == 59:
            clicking(815,yCoord)
    
    except:
        print("Button is not found")