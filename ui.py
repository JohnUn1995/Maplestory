import tkinter as tk

root = tk.Tk()
root.title('my window')
root.geometry('200x150')

def button_event():
    with open("main_test.py") as file:
       exec(open("main_test.py").read()) # exec() in python 3 is the equivalent of execfile() in python 2 #

mybutton1 = tk.Button(root, text='button', command=button_event)
mybutton2 = tk.Button(root, text='exit', command=root.destroy)
mybutton1.pack(side=tk.LEFT)
mybutton2.pack(side=tk.LEFT)

root.mainloop()