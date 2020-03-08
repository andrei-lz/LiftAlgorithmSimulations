class Lift:
    
    def __init__(self, posX: int, posY: int, width: int, height: int, speed: int, canvas):
        self.canvas = canvas
        self.width = width
        self.height = height
        self.posX = posX
        self.posY = posY
        self.speed = speed
        self.shape = canvas.create_rectangle(self.posX, self.posY, self.width, self.height, fill = "black")

    def moveUp(self):
        currentPos = self.canvas.coords(self.shape)
        self.canvas.move(self.shape, 0, -self.speed)

    def moveDown(self, xDest: int, yDest: int):
        currentPos = self.canvas.coords(self.shape)
        if (currentPos[3] != yDest):
            self.canvas.move(self.shape, 0, self.speed)
        return

class ElevatorShaft:

    def __init__(self, storeys: int, posX: int, posY: int, canvas, **kwargs):
        self.storeys = storeys
        self.scale = 1
        for param, value in kwargs.items():
            if param == "scale":
                self.scale = value
        
        self.liftsize = 100 * self.scale
        print(self.liftsize)
        self.width = self.liftsize
        self.height = self.liftsize * storeys
        self.canvas = canvas
        
        self.lift = Lift(self.liftsize, self.liftsize, posX + self.liftsize, posY +self.liftsize, 1, self.canvas)
        self.lift.canvas.create_rectangle(posX, posY, posX + self.width, posX + self.height)