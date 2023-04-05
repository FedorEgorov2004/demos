from PIL import Image, ImageDraw, ImageTk
from random import randint, choice
import tkinter as tk
from threading import Thread
from os import _exit

dots = []
c = randint(2, 15)

for i in range(c):
    dots.append([randint(0, 250), randint(0, 250)])

def network():
    global dots, label, img
    
    while True:
        img = Image.new('RGB', (250, 250), 'white')
        draw = ImageDraw.Draw(img)
        
        for i in range(c):
            x = randint(-1, 1)
            while not 1 < dots[i][0] + x < 250:
                x = randint(-1, 1)
            dots[i][0] += x
            
            x = randint(-1, 1)
            while not 1 < dots[i][1] + x < 250:
                x = randint(-1, 1)
            dots[i][1] += x
                
                
        for i in dots:
            for j in dots:
                if i != j:
                    draw.line((i[0], i[1], j[0], j[1]), fill = 0, width = 1)
        
        img = ImageTk.PhotoImage(img)
        label.config(image = img)
        label.image = img
    

def tv():
    global label, img
    
    while True:
        img = Image.new(size = (250, 250), mode = 'RGB', color = 'white')
        for y in range(img.size[1]):
            for x in range(img.size[0]):
                if randint(0, 1) == 0:
                    img.putpixel((x, y), (0, 0, 0))
        
        img = ImageTk.PhotoImage(img)
        label.config(image = img)
        label.image = img

root = tk.Tk()
root.geometry('250x250')
root.resizable(0, 0)
root.title('Network')

img = Image.new(size = (250, 250), mode = 'RGB', color = 'white')
img = ImageTk.PhotoImage(img)
label = tk.Label(root, image = img)
label.pack()

Thread(target = network).start()
root.protocol("WM_DELETE_WINDOW", lambda: _exit(0))

root.mainloop()