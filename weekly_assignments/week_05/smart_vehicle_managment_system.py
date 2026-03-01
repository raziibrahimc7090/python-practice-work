class Vehicle:
    def __init__(self, brand, speed, fuel_type):
        self.brand = brand
        self.speed = speed
        self.fuel_type = fuel_type

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Speed: {self.speed}")
        print(f"Fuel Type: {self.fuel_type}")


class Car(Vehicle):
    def __init__(self, brand, speed, fuel_type, number_of_doors):
        super().__init__(brand, speed, fuel_type)
        self.number_of_doors = number_of_doors

    def display_info(self):
        super().display_info()
        print(f"Number of Doors: {self.number_of_doors}")


class Bike(Vehicle):
    def __init__(self, brand, speed, fuel_type, engine_capacity):
        super().__init__(brand, speed, fuel_type)
        self.engine_capacity = engine_capacity

    def display_info(self):
        super().display_info()
        print(f"Engine Capacity: {self.engine_capacity}")


car = Car("Toyota", 180, "Petrol", 4)
bike = Bike("Yamaha", 120, "Petrol", "150cc")

print("Car Details:")
car.display_info()

print("\nBike Details:")
bike.display_info()
