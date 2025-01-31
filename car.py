class Car():
    def __init__(self, model, year, engineSize, color):
        self.model = model
        self.year = year
        self.engineSize = engineSize
        self.color = color
        self.speed = 0
        self.engineStarted = 0

    def drive(self):
        if self.engineStarted == 1:
            self.speed = 100
            print("The car is driving.")
        else:
            print("You need to start the engine before driving.")

    def stop(self):
        if self.engineStarted == 1 and self.speed > 0:
            self.speed = 0
            print("The car has stopped.")
        else:
            print("Either the cars enigne is not started or the speed is too low! Please do something")

    def startEngine(self):
        self.engineStarted = 1
        print("The car has started.")

    def stopEngine(self):
        if self.engineStarted == 1:
            self.engineStarted = 0

car = Car("Kia", 2015, 1.2, "Blue")
car.drive()
car.startEngine()
car.drive()