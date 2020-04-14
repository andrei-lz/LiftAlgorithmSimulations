from objects import Elevator

'''
Space for the algorithms/behaviours of elevators
'''

class Mechanical:

    def __init__(self, e: Elevator):
        e.lift.direction = "DOWN"

class Efficient:
    
    def __init__(self, e: Elevator):
        print(e)