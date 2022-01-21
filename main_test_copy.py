import pyautogui
import time
import keyboard
import pydirectinput
import random



import tkinter as tk

root = tk.Tk()
root.title('洗裝備腳本ByJohnUn')
root.geometry('200x150')

def runsomething():
    time.sleep(2)

    def randomClick(box):
        '''A function to return random click coordinates from box object by pyautogui'''
        x_click = int(random.uniform(box.left, box.left+box.width))
        y_click = int(random.uniform(box.top, box.top+box.height))
        return (x_click, y_click)

    location = pyautogui.locateOnScreen('location.png',grayscale=True,confidence=0.8)

    #location.left location.top w=165 h=270
    #pyautogui.click(randomClick(rand)(loli),duration=0.5)

    while 1:
        time.sleep(2)
        sure = pyautogui.locateOnScreen('sure.png',region=(location.left,location.top,165,270), grayscale=True,confidence=0.9)#偵測確定
        #sure_center = pyautogui.center(sure)
        pyautogui.click(randomClick(sure),duration=0.1)
        

        time.sleep(1)

        money_1 = pyautogui.locateOnScreen('money_1.png',region=(location.left,location.top,165,270), grayscale=True,confidence=0.9)#偵測10W

        if money_1 != None:
            pyautogui.press("esc")
        
            break
        else:
            ojbk = pyautogui.locateOnScreen('ojbk.png',region=(location.left,location.top,165,270), grayscale=True,confidence=0.9)#點OK
            #ojbk_center = pyautogui.center(ojbk)
            pyautogui.click(randomClick(ojbk),duration=0.1)
        

    print("End")


mybutton1 = tk.Button(root, text='洗裝備GOGOGO', command=runsomething)
mybutton2 = tk.Button(root, text='exit', command=root.destroy)
mybutton1.pack()
mybutton2.pack()

root.mainloop()


