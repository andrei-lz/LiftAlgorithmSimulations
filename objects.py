import tkinter as tk

class Elevator:
    
    def __init__(self, storeys: int, posX: int, posY: int, canvas):
        self.storeys = storeys
        self.posX = posX
        self.posY = posY
        self.width = 100
        self.height = 50
        self.storey_array = [canvas.create_rectangle(self.posX, self.posY + self.height * i, self.posX + self.width, self.posY + self.height * (i+1), fill="gray", activefill="yellow", state=tk.DISABLED) for i in range(0, storeys)]
        self.lift = Lift()
        self.canvas = canvas
    
    def update(self):
        for i in range(0, len(self.storey_array)):
            self.canvas.itemconfig(self.storey_array[i], fill = "gray")
        self.canvas.itemconfig(self.storey_array[self.storeys - 1 - self.lift.current_floor], fill="yellow")

class Lift:

    def __init__(self):
        self.capacity = 5
        self.current_floor = 0
    