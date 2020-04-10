from tkinter import *
import time
from objects import Elevator

def main():
    tk = Tk()

    width = 1000
    height = 800


    canvas = Canvas(tk, width = width, height = height)
    tk.title("Lift Simulation")
    canvas.pack()

    requests_generated = [[1], [10], [5, 2]]

    # Mechanical Elevator Implementation
    e_m = Elevator(10, 100, 100, canvas)
    e_m.lift.vel = 1

    while True:
        e_m.update()

        # Draw the requests for each floor
        for index in range(0, len(requests_generated)):
            person_count = Label(tk, text=len(requests_generated[index]), font=("Helvetica", 16), justify=LEFT)
            person_count.place(x=e_m.posX, y=100+50*index)


        tk.update()
        time.sleep(0.1)


if __name__ == "__main__":
    main()