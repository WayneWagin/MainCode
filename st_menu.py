import cv2
import numpy as np
import tkinter as tk


root = tk.Tk()
root.title('Eye of ender location')
XI, XII, YI, YII, DI, DII= tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar()

def conf():
    global LocA
    global LocB
    LocA = {'X': XI.get(), 'Y': YI.get(), 'DEG': DI.get()}
    LocB = {'X': XII.get(), 'Y': YII.get(), 'DEG': DII.get()}
    root.destroy()


def st_menu():
    img = np.zeros((500, 700, 3), np.uint8)
    img[:, :] = (150, 150, 150)


    XIlabel = tk.Label(root, text='X1:')
    XIlabel.grid(row=0, column=0)
    XIentry = tk.Entry(root, textvariable=XI)
    XIentry.grid(row=0, column=1)
    YIlabel = tk.Label(root, text='Y1:')
    YIlabel.grid(row=0, column=2)
    YIentry = tk.Entry(root, textvariable=YI)
    YIentry.grid(row=0, column=3)
    DIlabel = tk.Label(root, text='DEG1:')
    DIlabel.grid(row=0, column=4)
    DIentry = tk.Entry(root, textvariable=DI)
    DIentry.grid(row=0, column=5)

    XIIlabel = tk.Label(root, text='X2:')
    XIIlabel.grid(row=1, column=0)
    XIIentry = tk.Entry(root, textvariable=XII)
    XIIentry.grid(row=1, column=1)
    YIIlabel = tk.Label(root, text='Y2:')
    YIIlabel.grid(row=1, column=2)
    YIIentry = tk.Entry(root, textvariable=YII)
    YIIentry.grid(row=1, column=3)
    DIIlabel = tk.Label(root, text='DEG2:')
    DIIlabel.grid(row=1, column=4)
    DIIentry = tk.Entry(root, textvariable=DII)
    DIIentry.grid(row=1, column=5)

    confbutton = tk.Button(root, text='Confirm', command=conf)
    confbutton.grid(row=2, column=3)

    cv2.namedWindow("Stronghold Locater", cv2.WINDOW_AUTOSIZE)
    cv2.imshow('Stronghold Locater', img)
    root.mainloop()
    cv2.waitKey(0)
    cv2.destroyAllWindows()

