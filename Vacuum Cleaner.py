import random

def display_state(state):
    print("Room A:", "Clean" if state[0] == 0 else "Dirty", "| Room B:", "Clean" if state[1] == 0 else "Dirty")
    print("Vacuum Position:", "A" if state[2] == 0 else "B")

def vacuum_cleaner(state):
    print("Initial State:")
    display_state(state)
    while state[0] != 0 or state[1] != 0:
        if state[2] == 0: 
            if state[0] == 1:
                print("Cleaning Room A.")
                state[0] = 0
            else:
                print("Room A is Clean. Moving to Room B.")
                state[2] = 1
        else:
            if state[1] == 1:
                print("Cleaning Room B.")
                state[1] = 0
            else:
                print("Room B is Clean. Moving to Room A.")
                state[2] = 0
        display_state(state)
    print("Both Rooms are Clean!")

state = [random.randint(0, 1), random.randint(0, 1), random.randint(0, 1)]
vacuum_cleaner(state)
