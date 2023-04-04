from PIL import Image, ImageDraw, ImageTk
from random import randint, choice
import tkinter as tk
from threading import Thread
from os import _exit

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
root.title('TV')

img = Image.new(size = (250, 250), mode = 'RGB', color = 'white')
img = ImageTk.PhotoImage(img)
label = tk.Label(root, image = img)
label.pack()

Thread(target = tv).start()
root.protocol("WM_DELETE_WINDOW", lambda: _exit(0))

root.mainloop()
