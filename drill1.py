class Dog:
    def __init__(self, name, sound="woof"):
        self.name =name
        self.sound = sound
    def speak(self):
        print(f"{self.name} says {self.sound}")

if __name__ == "__main__":
    rex = Dog("Rex") 
    luna = Dog("Luna", sound="meow")
    rex.speak()
    luna.speak()           