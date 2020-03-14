from tkinter import *
import time
from objects import Elevator

tk = Tk()

height = 1000
width = 800

canvas = Canvas(tk, width = width, height = height)
tk.title("Lift Simulation")
canvas.pack()

e = Elevator(10, 1000, 100, canvas)

speed = 1
while True:
    
    tk.update()
    time.sleep(0.1)