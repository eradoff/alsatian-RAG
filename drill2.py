class Car:
    def __init__(self, make, model, year, sound="honk"):

        self.make = make
        self.model = model
        self.year = year
        self.sound = sound
    def drive(self):
        print(f"{self.make} {self.model} {self.year} sounds like {self.sound}")
        


if __name__ == "__main__":
    toyota = Car("Toyota", "Corolla", 2020, "vroom")
    mazda = Car("Mazda", "3", 2021, "beep")
    toyota.drive()
    mazda.drive()