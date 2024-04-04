import tkinter as tk
from tkinter import messagebox

def button_event():
    #print(var.get())
    if var.get() == '':
        tk.messagebox.showerror('message', '未輸入答案')
    elif var.get() == '2':
        tk.messagebox.showinfo('message', '答對了！')
    else:
        tk.messagebox.showerror('message', '答錯')

root = tk.Tk()
root.title('my window')

mylabel = tk.Label(root, text='1+1=')
mylabel.grid(row=0, column=0)

var = tk.StringVar()
myentry = tk.Entry(root, textvariable=var)
myentry.grid(row=0, column=1)

mybutton = tk.Button(root, text='完成', command=button_event)
mybutton.grid(row=1, column=1)

root.mainloop()