from random import random
from tkinter import IntVar
from tkinter import StringVar
import tkinter as tk
import os
import sys


def resource_path(relative_path):
    absolute_path = os.path.abspath(__file__)
    root_path = os.path.dirname(absolute_path)
    base_path = getattr(sys, '_MEIPASS', root_path)
    return os.path.join(base_path, relative_path)

# to package using pyinstaller
# run, pyinstaller --onefile --noconsole --add-binary <image>.<gif>;. <script>.py
# for multiple binary files, try --add-binary <image>.<gif>;. -add-binary <image2>.<gif>;.   and so on


window = tk.Tk()
window.geometry('400x400')

bg_img = tk.PhotoImage(file=resource_path('./images/sunset.gif'))
bg_Lbl = tk.Label(window, image=bg_img)
bg_Lbl.place(x=0, y=0, relwidth=1, relheight=1)


big_img = tk.PhotoImage(file=resource_path('./images/eyeopener.gif'))
img = tk.PhotoImage.subsample(big_img, x=4, y=4)

vq = StringVar()
vq.set('question')
score = IntVar()
score.set(0)
lives = IntVar()
lives.set(3)
sl_Lbl = StringVar()

sl_Lbl.set('Score: {} Lives: {} '.format(score.get(), lives.get()))

imgLbl = tk.Label(window, image=img)
lq = tk.Label(window, textvariable=vq,
              relief='groove', width=20, wraplength=250)

la = tk.Entry(window, relief='groove', width=15)
ls = tk.Label(window, textvariable=sl_Lbl, relief='groove', width=20)
# buttons for submitting answers and new questions
sa = tk.Button(window)
nq = tk.Button(window)

imgLbl.grid(row=0, column=0, sticky='W')
lq.grid(row=0, column=1, sticky='NW', padx=2)
la.grid(row=0, column=2, sticky='NE', padx=2)
ls.grid(row=0, column=1, pady=4, padx=2)
sa.grid(row=2, column=0, sticky='NW', padx=2)
nq.grid(row=1, column=0, sticky='NW', padx=2)

window.title('Multiplication Practice')
window.resizable(0, 0)

sa.configure(text='Submit answer', bg='blue')
nq.configure(text='New Question', bg='blue')

correctanswer = IntVar()
correctanswer.set(0)


def newq():
    x = int(random()*10)
    y = int(random()*10)

    correctanswer.set(x*y)

    vq.set('What is {} * {}?'.format(x, y))

    nq.configure(state='disabled')
    sa.configure(state='normal')


def checka():
    if (int(la.get()) == correctanswer.get()):
        score.set(score.get() + 1)
    else:
        lives.set(lives.get() - 1)
    sl_Lbl.set('Score: {} Lives: {} '.format(score.get(), lives.get()))
    if(lives.get() == 0):
        window.destroy()

    nq.configure(state='normal')
    sa.configure(state='disabled')


nq.configure(command=newq)
sa.configure(command=checka)


window.mainloop()
