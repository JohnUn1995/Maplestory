import pyautogui
import time
import keyboard
import pydirectinput
import random
import os
import base64
import tkinter as tk

from money_1_png import img as money_1_1   #导入第一张图片的py文件，重命名为one
from location_png import img as location_1   #导入第一张图片的py文件，重命名为two
from ojbk_png import img as ojbk_1   #导入第一张图片的py文件，重命名为one
from sure_png import img as sure_1



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

    #先把图片弄出来
    tmp = open('money_1.png', 'wb')        #创建临时的文件, 这里把后缀改成了gif，因为tk只认识gif格式图片
    tmp.write(base64.b64decode(money_1_1))    ##把这个one图片解码出来，写入文件中去。
    tmp.close()  
    tmp2 = open('location.png', 'wb')        #创建临时的文件,这里把后缀改成了gif，因为tk只认识gif格式图片
    tmp2.write(base64.b64decode(location_1))    ##把这个two图片解码出来，写入文件中去。
    tmp2.close()
    tmp2 = open('ojbk.png', 'wb')        #创建临时的文件,这里把后缀改成了gif，因为tk只认识gif格式图片
    tmp2.write(base64.b64decode(ojbk_1))    ##把这个two图片解码出来，写入文件中去。
    tmp2.close()
    tmp2 = open('sure.png', 'wb')        #创建临时的文件,这里把后缀改成了gif，因为tk只认识gif格式图片
    tmp2.write(base64.b64decode(sure_1))    ##把这个two图片解码出来，写入文件中去。
    tmp2.close()

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
        
    os.remove('money_1.png')
    os.remove('sure.png')
    os.remove('ojbk.png')
    os.remove('location.png')
    print("End")


mybutton1 = tk.Button(root, text='洗裝備GOGOGO', command=runsomething)
mybutton2 = tk.Button(root, text='exit', command=root.destroy)
mybutton1.pack()
mybutton2.pack()

root.mainloop()


