# Créé par GamingFun, le 08/01/2021 en Python 3.7

from tkinter import *
import random

fenetre = Tk()

label = Label(fenetre, text="Hello, World")
label.pack()

canvas = Canvas(fenetre, width=400, height=400)
canvas.pack()

def random_color():
    return random.randint(0,0x1000000)

def restart():
    canvas.delete("all")
    for x in range(0, random.randint(0,500)):
        color = '{:06x}'.format(random_color())
        x1 = random.randint(0,400)
        y1 = random.randint(0,400)
        x2 = random.randint(0,400)
        y2 = random.randint(0,400)
        ligne = canvas.create_polygon(x1, y1, x2, y2,\
            fill =('#'+ color), outline='#'+ color)

for x in range(0, random.randint(0,500)):

    color = '{:06x}'.format(random_color())
    x1 = random.randint(0,400)
    y1 = random.randint(0,400)
    x2 = random.randint(0,400)
    y2 = random.randint(0,400)
    ligne = canvas.create_polygon(x1, y1, x2, y2,\
        fill =('#'+ color), outline='#'+ color)

Bouton_sortie = Button(fenetre, text="RageQuit", command=fenetre.destroy)
Bouton_sortie.pack()

Bouton_restart = Button(fenetre, text="Restart", command=restart)
Bouton_restart.pack()

fenetre.mainloop()
