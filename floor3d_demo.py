from PIL import Image, ImageDraw, ImageTk
from random import randint
from os import _exit
import tkinter as tk
from threading import Thread
from time import sleep

xp = 9 # перспектива
yp = 15 # перспектива
y0 = 5 # константа y верхняя
y1 = 90 # константа y нижняя
m = 200 # marginx
my = 30 # marginy
sx = 400
sy = 200

# Инициализация
x = [[i * xp, y0, i * yp, y1] for i in range(10)]
im = Image.new(size = (sx, sy), mode = 'RGB', color = 'white')
dr = ImageDraw.Draw(im)

# Рисуем (1 строка - оригинал, 2 - "зеркало")
for i in x:
    dr.line([i[j] + m if j % 2 == 0 else i[j] + my for j in range(len(i))], fill = (255, 0, 0))
    dr.line([-i[j] + m if j % 2 == 0 else i[j] + my for j in range(len(i))], fill = (255, 0, 0))

# Построение границ
for i in range(-x[-1][0] + m, x[-1][0] + m + 1): # Верхняя
    p = im.getpixel((i, y0))
    color = (int(p[0] / 2), int(p[1] / 2), int((p[2] + 255) / 2))
    im.putpixel((i, y0), (color))

for y in range(0, sy, 10): # Нижняя
    for i in range(-x[-1][2] + m, x[-1][2] + m + 1):
        p = im.getpixel((i, y))
        color = (int(p[0] / 2), int(p[1] / 2), int((p[2] + 255) / 2))
        im.putpixel((i, y), (color))

# Проводим линии для точек
dots = []
for y in range(0, sy):
    mt = []
    for i in range(0, sx):
        if im.getpixel((i, y)) == (127, 0, 127):
            mt.append([i, y])
    dots.append(mt)

dots = str(eval(str(dots).replace("[], ", ""))[0:-1])

def draw():
    img_ = Image.new(size = (sx, sy), mode = 'RGB', color = 'white')
    dr_ = ImageDraw.Draw(img_)
    dots2 = eval(dots)

    for j in range(len(dots2[0])):
        dy = randint(-15, 15)
        for i in range(len(dots2)):
            dots2[i][j][1] += dy

    for i in range(len(dots2)):
        for j in range(len(dots2[0])):
            dx = randint(-5, 5)
            dots2[i][j][1] += dx
    
    dots2 = eval(str(dots2).replace('[', '(').replace(']', ')'))
    for i in range(len(dots2)):
        dr_.line(xy = [j for j in dots2[i]], fill = 'black')
    for i in range(len(dots2[0])):
        dr_.line(xy = [j[i] for j in dots2], fill = 'black')
        
    return img_

root = tk.Tk()
root.geometry('400x200')
root.resizable(0, 0)
root.title('floor3D demo')
img = ImageTk.PhotoImage(draw())
label = tk.Label(root, image = img)
label.pack()

def gi():
    while True:
        img = ImageTk.PhotoImage(image = draw())
        label.config(image = img)
        label.image = img
        sleep(0.01667)
            
root.protocol("WM_DELETE_WINDOW", lambda: _exit(0))
Thread(target = gi).start()

root.mainloop()