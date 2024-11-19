class Device:
    def __init__(self,height,width,name):
        self.name=name
        self.height=height
        self.width=width
    def power_on(self):
        print("Device has powered on")

class Computer(Device):
    def power_on(self):
        print("Computer has powered on")
    def fix(self):
        print("Computer is being fixed")
    def poweroff(self):
        print("Computer is powering off")
class Vehicle:
    def __init__(self,name,speed,size):
        self.name=name
        self.speed=speed
        self.size=size
    def switch_on(self):
        print("Vehicle has switched on")
    def drive(self):
        print("Vehicle is driving")
    def fix(self):
        print("Vehicle is being fixed")
class car(Vehicle):
    def switch_on(self):
        print("Car has switched on")
    def drive(self):
        print("Car is driving")
    def fix(self):
        print("Car is being fixed")
    def filltank(self):
        print("Car is being filled with gas")
class motorbike(Vehicle):
    def switch_on(self):
        print("Motorbike is being switched on")
    def drive(self):
        print("Motorbike is driving")
    
