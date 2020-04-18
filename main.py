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

    requests_generated = [[1], [9], [5, 2],[9,2,3,2,1],[],[],[],[],[],[]]

    # Mechanical Elevator Implementation
    e_m = Elevator(10, 100, 100, canvas)
    e_m.lift.vel = 1
    drawFloors(tk, e_m)
    e_m_title = Label(tk, text="Base Case Algorithm", font=("Impact", 24), justify=LEFT)
    e_m_title.place(x=e_m.posX, y=e_m.posY-e_m.height-25)
    e_m_TOTAL_TIME = 0
    e_m_REQUESTS = [[1], [9], [5, 2],[9,2,3,2,1],[],[],[],[],[],[]]
    e_m_requests_left = 0
    for index in e_m_REQUESTS:
        e_m_requests_left += len(index)

    # Free Elevator Implementation
    e_f = Elevator(10, 500, 100, canvas)
    e_f.lift.vel = 1
    drawFloors(tk, e_f)
    e_f_title = Label(tk, text="Improved Algorithm", font=("Impact", 24), justify=LEFT)
    e_f_title.place(x=e_f.posX, y=e_f.posY-e_f.height-25)
    e_f_TOTAL_TIME = 0
    e_f_REQUESTS = [[1], [9], [5, 2],[9,2,3,2,1],[],[],[],[],[],[]]
    e_f_requests_left = 0
    for index in e_f_REQUESTS:
        e_f_requests_left += len(index)

    while True:
        e_m.update()
        e_f.update()
        # Draw the requests for each floor
        drawRequests(tk, e_m, e_m_REQUESTS)

        drawRequests(tk, e_f, e_f_REQUESTS)

        ### BEHAVIOURS ###

        ##
        ## Mechanical Elevator
        ##

        if e_m_requests_left > 0:
            #Set the correct direction (only changes at the top or bottom)
            if e_m.lift.current_floor == e_m.storeys - 1:
                e_m.lift.direction = "UP"
            elif e_m.lift.current_floor == 0:
                e_m.lift.direction = "DOWN"
                
            # Boarding Passengers
            if len(e_m_REQUESTS[e_m.lift.current_floor]) > 0:
                print(e_m_REQUESTS[e_m.lift.current_floor])
                for passenger in e_m_REQUESTS[e_m.lift.current_floor][:]:
                    if e_m.lift.capacity > 0:
                        e_m.lift.addPassenger(passenger)
                        e_m_TOTAL_TIME += board_time
                        e_m_REQUESTS[e_m.lift.current_floor].remove(passenger)
            
            # Move the elevator up or down, however it's allowed
            if e_m.lift.direction == "DOWN":
                e_m.lift.current_floor += 1
            else:
                e_m.lift.current_floor -= 1
            e_m_TOTAL_TIME += move_time

            # Drop Passengers off at the floor they want
            if len(e_m.lift.passengers) > 0:
                for passenger in e_m.lift.passengers:
                    if passenger == e_m.lift.current_floor:
                        e_m.lift.removePassenger(passenger)
                        e_m_TOTAL_TIME += board_time
                        e_m_requests_left -= 1
                        print("Dropping off passenger at", passenger)
        else:
            win_f = Label(text="DONE IN "+str(e_m_TOTAL_TIME)+" seconds!")
            win_f.place(x=e_m.posX+200, y=e_m.posY)
            
        ##
        ## Free Elevator
        ##
        if e_f_requests_left > 0:

            # Drop Passengers off at the floor they want
            if len(e_m.lift.passengers) > 0:
                for passenger in e_f.lift.passengers:
                    if passenger == e_f.lift.current_floor:
                        e_f.lift.removePassenger(passenger)
                        e_f_TOTAL_TIME += board_time
                        e_f_requests_left -= 1
                        print("Dropping off passenger at", passenger)

            # Board Passengers
            if len(e_f_REQUESTS[e_f.lift.current_floor]) > 0:
                print("There are",len(e_f_REQUESTS[e_f.lift.current_floor]), "passengers on floor", 10-e_f.lift.current_floor)
                print(e_f_REQUESTS[e_f.lift.current_floor])
                for passenger in e_f_REQUESTS[e_f.lift.current_floor][:]:
                    if e_f.lift.capacity > 0:
                        print("lift has space!")
                        e_f.lift.addPassenger(passenger)
                        print("Boarding passenger")
                        e_f_TOTAL_TIME += board_time
                        e_f_REQUESTS[e_f.lift.current_floor].remove(passenger)
            
            #Sort the passenger requests in terms of proximity to the current floor
            #Important for the algorithm to do the least steps to drop someone off
            #Heading towards the furthest one away means it's likely to meet the others
            # - on the way
            if e_f.lift.capacity > 1:
                e_f.lift.passengers.sort(key=lambda x: abs(e_f.lift.current_floor-x))
                e_f.lift.passengers.reverse()
            
            # Move the elevator closer to the next destination
            # If the elevator is empty, go for requests
            if e_f.lift.capacity >= 5:
                # requests
                print("re")
            # Otherwise go for passenger destinations
            else:
                if (e_f.lift.passengers[0] - e_f.lift.current_floor) < 0:
                    e_f.lift.current_floor -= 1
                else:
                    e_f.lift.current_floor += 1

        else:
            win_f = Label(text="DONE IN "+str(e_f_TOTAL_TIME)+" seconds!")
            win_f.place(x=e_f.posX+200, y=e_f.posY)

        tk.update()
        time.sleep(.02)


def drawRequests(tk: Tk, e: Elevator, requests_gen: list) -> None:
    '''
    Displays the requests/people calling the elevator for each floor of the elevator
    '''
    for index in range(0, len(requests_gen)):
            person_count = Label(tk, text=len(requests_gen[index]), font=("Helvetica", 16), justify=LEFT)
            person_count.place(x=e.posX-20, y=100+50*index)

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