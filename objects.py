class Elevator:
    
    def __init__(self, storeys: int, posX: int, posY: int, canvas):
        self.posX = posX
        self.posY = posY
        self.width = 100
        self.height = 50
        self.storey_array = [canvas.create_rectangle(self.posX, self.posY+(self.height*i), self.posX+self.width, self.height + self.posY+(self.height*i), fill = "gray") for i in range(0, storeys)]
