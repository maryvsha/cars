class TownCar:
    def __init__(self, speed, colour, name, is_police, direction):
        self.speed = speed
        self.colour = colour
        self.name = name
        self.is_police = is_police
        self.direction = direction

    def go(self):
        return "Car's started"

    def stop(self):
        return "Car's stopped"

    def turn(self):
        return f"Car turned to the {self.direction}"

class SportCar:
    def __init__(self, speed, colour, name, is_police, direction):
        TownCar.__init__(self, speed, colour, name, is_police)
    def go(self):
        return "Car's started"

    def stop(self):
        return "Car's stopped"

    def turn(self):
        return f"Car turned to the {self.direction}"

class WorkCar:
    def __init__(self, speed, colour, name, is_police, direction):
        TownCar.__init__(self, speed, colour, name, is_police)

    def go(self):
        return "Car's started"

    def stop(self):
        return "Car's stopped"

    def turn(self):
        return f"Car turned to the {self.direction}"

class PoliceCar:
    def __init__(self, speed, colour, name, is_police, direction):
        TownCar.__init__(self, speed, colour, name, is_police)
    
    def go(self):
        return "Car's started"

    def stop(self):
        return "Car's stopped"

    def turn(self):
        return f"Car turned to the {self.direction}"

car1 = TownCar("322", "blue", "BMW", True, "left")
print(car1.go(), car1.stop(), car1.turn())