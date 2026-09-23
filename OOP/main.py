class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def get_info(self):
        return f"{self.brand} {self.model} ({self.year})"

class Car(Vehicle):
    def __init__(self, brand, model, year, doors):
        super().__init__(brand, model, year)
        self.doors = doors

    def get_info(self):
        return super().get_info() + f" - {self.doors} doors"

class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, engine_cc):
        super().__init__(brand, model, year)
        self.engine_cc = engine_cc

    def get_info(self):
        return super().get_info() + f" - {self.engine_cc}cc"

vehicles = [
    Car("BMW", "M3", 2024, 4),
    Motorcycle("Kawasaki", "Ninja", 2022, 1000),
    Car("Audi", "RS6", 2023, 5),
    Motorcycle("Yamaha", "R1", 2023, 1000)
]

for vehicle in vehicles:
    print(vehicle.get_info())