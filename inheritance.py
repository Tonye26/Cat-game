class Animal:
    def __init__(self,given_name,given_colour):
        self.name=given_name
        self.colour=given_colour
    def make_noise(self):
        print("Animal made a noise!")

class OrcaWhale(Animal):
    def __init__(self, given_name, given_colour):
        super().__init__(given_name, given_colour)
        self.fins=3
    #Overriding
    def make_noise(self):
        print("OOOO!")
    def swim(self):
        print("Orca is swimming!")

cat=Animal("Bob","Black")
orca=OrcaWhale("Jimmy","White")
cat.make_noise()
orca.make_noise()
orca.swim