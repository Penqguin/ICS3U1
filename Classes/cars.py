class Car:
  def __init__(self, make='', model='', colour='', year= 2000, milage = 0, fuel = 20):
    self.make = make
    self.model = model
    self.colour = colour
    self.year = year
    self.milage = milage
    self.fuel = fuel
  
  def displayInfo(self):
    return f"{self.make} {self.model} {self.colour} {self.year}"

  def displayMilage(self):
    return self.milage

  def isLuxury(self):
    return False
  
  def refuel(self):
    if self.fuel/50 < 25: #in percentage
      print(f"you should refuel your car")
    else:
      print(f"no need to refuel")
  
  def fuelLeft(self, distance):
    fuelLeft = self.fuel - (distance / 10)
    return f"{fuelLeft} liters"

  def distanceLeft(self):
    return self.fuel * 10

class Luxury_Cars(Car):
  def isLuxury(self):
    return True


toyotaCamry = Car("Toyota", "Camry", "White", 2010, 1200)
hondaCivic = Car("Honda", "Civic", "Red", 2019, 2200)
teslaCybertruck = Car("Tesla", "Cyber Truck", "silver", 2024, 4910)
lamborgini = Luxury_Cars('lamborgini', 'hurican', 'black', 2020, 1000)

print(lamborgini.fuelLeft(int(input("distance traveled: "))))

print(lamborgini.displayInfo(), lamborgini.displayMilage(), lamborgini.isLuxury())
print(hondaCivic.displayInfo(), hondaCivic.displayMilage(), hondaCivic.isLuxury())