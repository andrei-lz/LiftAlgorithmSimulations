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
    # Time settings for how long it takes to board a passenger or
    # Move to a different floor in seconds
    move_time = 10
    board_time = 3
    
    # Setting up tkinter and a canvas for drawing

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
    e_m_requests_left = 0
    for index in requests_generated:
        e_m_requests_left += len(index)
    e_m_TOTAL_TIME = 0

    e_f = Elevator(10, 500, 100, canvas)
    e_f.lift.vel = 1
    drawFloors(tk, e_f)
    e_f_title = Label(tk, text="Improved Algorithm", font=("Impact", 24), justify=LEFT)
    e_f_title.place(x=e_f.posX, y=e_f.posY-e_f.height-25)
    e_f_requests_left = e_m_requests_left # They start off with the same requests
    e_f_TOTAL_TIME = 0

    while True:
        e_m.update()
        e_f.update()
        # Draw the requests for each floor
        drawRequests(tk, e_m, requests_generated)

        drawRequests(tk, e_f, requests_generated)

        ### BEHAVIOURS ###

        ## Mechanical Elevator

        if e_m_requests_left > 0:
            #Set the correct direction (only changes at the top or bottom)
            e_m.lift.direction = "DOWN"
            if e_m.lift.current_floor == e_m.storeys - 1:
                e_m.lift.direction = "UP"
                
            # Board Passengers
            if len(requests_generated[e_m.lift.current_floor]) > 0:
                for passenger in requests_generated[e_m.lift.current_floor]:
                    e_m.lift.addPassenger(passenger)
                    e_m_requests_left -= 1
                    e_m_TOTAL_TIME += board_time
                    print(e_m.lift.current_floor, e_m.lift.passengers, e_m_requests_left, e_m_TOTAL_TIME)
            
            # Move the elevator up or down, however it's allowed
            if e_m.lift.direction == "DOWN":
                e_m.lift.current_floor += 1
            else:
                e_m.lift.current_floor -= 1
            e_m_TOTAL_TIME += move_time

            # Drop Passengers off at the floor they want
            for passenger in e_m.lift.passengers:
                if passenger == e_m.lift.current_floor:
                    e_m.lift.removePassenger(passenger)
                    e_m_TOTAL_TIME += board_time



        tk.update()
        time.sleep(.5)


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