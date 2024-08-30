from abc import ABC, abstractmethod

# ----------------------------Class vehicle------------------------------#
class Vehicle(ABC):
    def __init__(self):
        self.gear = 0
        self.engine_running = False

    @abstractmethod
    def clutch(self):
        pass

    @abstractmethod
    def brake(self):
        pass

    @abstractmethod
    def accelerator(self):
        pass

    def change_gear(self, gear):
        self.gear = gear
        print(f"Gear changed to {self.gear}")

    def start_engine(self):
        if not self.engine_running:
            self.engine_running = True
            print("Engine started")
        else:
            print("Engine is already running")

    def stop_engine(self):
        if self.engine_running:
            self.engine_running = False
            print("Engine stopped")
        else:
            print("Engine is already stopped")

# ---------------------------Car----------------------------#
class Car(Vehicle):
    def clutch(self):
        if self.engine_running:
            print("Car clutch engaged")
        else:
            print("Start the engine first")

    def brake(self):
        if self.engine_running:
            print("Car brake applied")
        else:
            print("Start the engine first")

    def accelerator(self):
        if self.engine_running:
            print("Car accelerator pressed")
        else:
            print("Start the engine first")

#--------------------------------Bike------------------------#
class Bike(Vehicle):
    def clutch(self):
        if self.engine_running:
            print("Bike clutch engaged")
        else:
            print("Start the engine first")

    def brake(self):
        if self.engine_running:
            print("Bike brake applied")
        else:
            print("Start the engine first")

    def accelerator(self):
        if self.engine_running:
            print("Bike accelerator pressed")
        else:
            print("Start the engine first")

#------------------------------------Display Choice-------------------#
def operate_vehicle(vehicle):
    vehicle.start_engine()
    while True:
        print("\nChoose an action:")
        print("1. Engage clutch")
        print("2. Apply brake")
        print("3. Press accelerator")
        print("4. Change gear")
        print("5. Stop engine")
        print("6. Exit")

        choice = input("Enter the number of your choice: ")

        if choice == '1':
            vehicle.clutch()
        elif choice == '2':
            vehicle.brake()
        elif choice == '3':
            vehicle.accelerator()
        elif choice == '4':
            gear = int(input("Enter the gear number: "))
            vehicle.change_gear(gear)
        elif choice == '5':
            vehicle.stop_engine()
            break  
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

# -----------------------------Main----------------------------------#
def main():
    while True:
        print("\nWhich vehicle would you like to operate?")
        print("1. Car")
        print("2. Bike")
        print("3. Exit")

        vehicle_choice = input("Enter the number of your choice: ")

        if vehicle_choice == '1':
            vehicle = Car()
            print("Operating Car:")
            operate_vehicle(vehicle)
        elif vehicle_choice == '2':
            vehicle = Bike()
            print("Operating Bike:")
            operate_vehicle(vehicle)
        elif vehicle_choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
