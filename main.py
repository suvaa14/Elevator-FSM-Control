import time
from enum import Enum, auto

class ElevatorState(Enum):
    IDLE = auto()
    MOVING_UP = auto()
    MOVING_DOWN = auto()
    DOOR_OPEN = auto()

class Elevator:
    def __init__(self, floors=5):
        self.state = ElevatorState.IDLE
        self.current_floor = 1
        self.target_floor = None
        self.total_floors = floors

    def display_status(self):
        print(f"[{self.state.name}] Elevator at Floor {self.current_floor}")

    def get_user_input(self):
        while True:
            try:
                choice = int(input(f"\nEnter target floor (1-{self.total_floors}, or 0 to quit): "))
                if choice == 0:
                    return 'exit'
                if 1 <= choice <= self.total_floors and choice != self.current_floor:
                    return choice
                else:
                    print("[!] Invalid floor or already on this floor.")
            except ValueError:
                print("[!] Please enter a number.")

    def move_elevator(self):
        if self.current_floor < self.target_floor:
            self.state = ElevatorState.MOVING_UP
            while self.current_floor < self.target_floor:
                self.current_floor += 1
                self.display_status()
                time.sleep(1)
        elif self.current_floor > self.target_floor:
            self.state = ElevatorState.MOVING_DOWN
            while self.current_floor > self.target_floor:
                self.current_floor -= 1
                self.display_status()
                time.sleep(1)
        self.state = ElevatorState.DOOR_OPEN
        self.display_status()

    def open_door(self):
        print("🚪 Door opening...")
        time.sleep(2)
        print("✅ You have arrived at your destination.")
        time.sleep(2)
        print("🚪 Door closing...")
        time.sleep(1)

    def run(self):
        print("🏢 Elevator Simulation Started\n")
        try:
            while True:
                self.state = ElevatorState.IDLE
                self.display_status()
                user_input = self.get_user_input()
                if user_input == 'exit':
                    print("🚪 Elevator shutting down. Goodbye!")
                    break
                self.target_floor = user_input
                self.move_elevator()
                self.open_door()
        except KeyboardInterrupt:
            print("\n[!] Interrupted. Elevator stopping.")

if __name__ == "__main__":
    elevator = Elevator(floors=5)
    elevator.run()
