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

        for floor in requests_generated:
            for person in floor:
                print(person)
            print("mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm")


        tk.update()
        time.sleep(0.1)


if __name__ == "__main__":
    main()