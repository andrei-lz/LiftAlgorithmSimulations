from tkinter import *
import time
from objects import Elevator

tk = Tk()

width = 1000
height = 800


canvas = Canvas(tk, width = width, height = height)
tk.title("Lift Simulation")
canvas.pack()

e = Elevator(10, 100, 100, canvas)

speed = 1
while True:
    e.update()
    tk.update()
    time.sleep(0.1)