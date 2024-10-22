# car.py

class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        return "Engine started"

    def stop(self):
        return "Engine stopped"


class FuelSystem:
    def __init__(self, fuel_level):
        self.fuel_level = fuel_level

    def refuel(self, amount):
        self.fuel_level += amount
        return f"Fuel level: {self.fuel_level}"


class Car:
    def __init__(self, engine, fuel_system):
        self.engine = engine
        self.fuel_system = fuel_system

    def start(self):
        if self.fuel_system.fuel_level > 0:
            return self.engine.start()
        else:
            return "Cannot start, no fuel"

    def stop(self):
        return self.engine.stop()
