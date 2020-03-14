from tkinter import *
import time
from objects import Lift, ElevatorShaft

tk = Tk()

height = 1000
width = 800

canvas = Canvas(tk, width = width, height = height)
tk.title("Lift Simulation")
canvas.pack()
#l = canvas.create_rectangle(100, 100, 200, 200, fill = "black")

objects = []

system = ElevatorShaft(10, 100, 100, canvas, scale=0.5)
l = system.lift

objects.append(l)

speed = 1
while True:
    
    tk.update()
    time.sleep(0.1)