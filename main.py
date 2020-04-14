'''
Simulation to compare times of two different elevator algorithms
'''

from tkinter import Tk, Canvas, Label, LEFT
import time
from objects import Elevator

def main():
    '''
    Application entry point
    Sets up 2 elevators and some labels for the simulation
    Contains the main loop for TKinter graphical display
    '''
    tk = Tk()

    width = 1366
    height = 800


    canvas = Canvas(tk, width = width, height = height)
    tk.title("Lift Simulation")
    canvas.pack()

    requests_generated = [[1], [10], [5, 2]]

    # Mechanical Elevator Implementation
    e_m = Elevator(10, 100, 100, canvas)
    e_m.lift.vel = 1
    drawFloors(tk, e_m)
    e_m_title = Label(tk, text="Base Case Algorithm", font=("Impact", 24), justify=LEFT)
    e_m_title.place(x=e_m.posX, y=e_m.posY-e_m.height-25)

    e_f = Elevator(10, 500, 100, canvas)
    e_f.lift.vel = 1
    drawFloors(tk, e_f)
    e_f_title = Label(tk, text="Improved Algorithm", font=("Impact", 24), justify=LEFT)
    e_f_title.place(x=e_f.posX, y=e_f.posY-e_f.height-25)

    while True:
        e_m.update()
        e_f.update()
        # Draw the requests for each floor
        drawRequests(tk, e_m, requests_generated)

        drawRequests(tk, e_f, requests_generated)

        tk.update()
        time.sleep(0.2)


def drawRequests(tk: Tk, e_m: Elevator, requests_generated: list) -> None:
    '''
    Displays the requests/people calling the elevator for each floor of the elevator
    '''
    for index in range(0, len(requests_generated)):
            person_count = Label(tk, text=len(requests_generated[index]), font=("Helvetica", 16), justify=LEFT)
            person_count.place(x=e_m.posX, y=100+50*index)

def drawFloors(tk: Tk, e: Elevator) -> None:
    '''
    Displays the floor numbers of the elevator
    '''
    floors = e.storeys
    offX = e.posX + e.width + 5
    for floor in range(floors, 0, -1):
        offY = e.posY + e.height*(floor-1)
        l = Label(tk, text="Floor "+str(floors + 1 - floor), font=("Helvetica", 18), justify=LEFT)
        l.place(x=offX, y=offY)

if __name__ == "__main__":
    main()