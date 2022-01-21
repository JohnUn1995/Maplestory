import pyautogui
import time
import keyboard
import random

#maplestorylocation = pyautogui.locatOnScreen('maplestory.png',grayscale=True,confindence=0.8)

while 1:
    if pyautogui.locateOnScreen('1_2.png',grayscale=True,confidence=0.9) != None:
        print("i can see it")
        time.sleep(0.5)
        
    else:
        print("i am unable to see it")
        time.sleep(0.5)


