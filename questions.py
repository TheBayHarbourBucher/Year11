#---begin Python ---
class Car:
    def __init__(self, make, model, year, colour):
        self.make = make
        self.model = model
        self.year = year
        self.colour = colour
    
    def start(self):
        print(f"{self.make} {self.model} is starting.")

    def stop(self):
        print(f"{self.make} {self.model} is stopping.")

# Instantiating objects from the Car class
car1 = Car("Toyota", "Camry", 2020, "Red")
car2 = Car("Honda", "Civic", 2018, "Blue")

car1.start()  # Output: Toyota Camry is starting.
car2.stop()   # Output: Honda Civic is stopping.
#--- end python ---

#adding instances for the car class
car3 = Car("Tesla", "ELectric", 2099, "Magento")


print(car3.make)   #output - tesla
print(car3.model)  #output - electric
print(car3.year)    #output - 2099
print(car3.colour)  #output -Magento

def start(self):
    print(f"{self.make} {self.model} is starting.") #to print the message the car is starting

# sub class
class SilentCar(Car):
    def __init__(self, make, model, year, colour, battery_capacity):
        super().__init__(make, model, year, colour)
        self.battery_capacity = battery_capacity

    def start(self):
        print(f"{self.make} {self.model} is starting silently.")

#adding instances for the car class
car1 = Car("Toyota", "Camry", 2020, "Red")
car2 = SilentCar("Tesla", "Model S", 2022, "White", "100 kWh")

#the output
print(car1.start())  # starting
print(car2.start())  #strarting silently