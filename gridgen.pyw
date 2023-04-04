from PIL import Image, ImageDraw, ImageTk
from random import randint, choice
import numpy as np
import tkinter as tk
from threading import Thread
from time import sleep
from os import _exit

def get_grid2(w, h, s, f):
    a = [[[i, j] for j in range(100, 100 + w * s + 1, s)] for i in range(100, 100 + h * s + 1, s)]
    
    im = Image.new(size = (a[-1][-1][0] + 100, a[-1][-1][1] + 100), mode = 'RGB', color = 'black')
    dw = ImageDraw.Draw(im)
    
    for i in range(h + 1):
        dy = randint(-10, 10)
        for j in range(w + 1):
            a[i][j][1] += dy
            
    for i in range(w + 1):
        dx = randint(-2, 2)
        for j in range(h + 1):
            a[i][j][0] += randint(-2, 2)
    
    x = eval(str(a).replace('[', '(').replace(']', ')'))
    
    for i in range(len(x)):
        dw.line(xy = [j for j in x[i]], fill = f)
    for i in range(len(x[0])):
        dw.line(xy = [j[i] for j in x], fill = f)
            
    return im

g = Image.open('spectrum.png')
c = []
for i in range(g.size[0]):
    c.append(g.getpixel((i, 7)))
c = list(c)
c += list(reversed(c[:-1]))

root = tk.Tk()
root.geometry('300x300')
root.resizable(0, 0)
root.title('Gridgen demo')
img = ImageTk.PhotoImage(get_grid2(10, 10, 10, (0, 0, 0)))
label = tk.Label(root, image = img)
label.pack()

def gi():
    global label, img
    
    while True:
        for i in c:
            img = ImageTk.PhotoImage(get_grid2(10, 10, 10, i))
            label.config(image = img)
            label.image = img
            # sleep(0.01667)

root.protocol("WM_DELETE_WINDOW", lambda: _exit(0))
Thread(target = gi).start()

print('start')

root.mainloop()
