class address():
  def __init__(self, streetName='Finch Ave West', streetNum='550', city='North York', province='Ontario', postalCode='M2R1N6'):
    self.streetName = streetName
    self.streetNum = streetNum
    self.city = city
    self.province = province
    self.postalCode = postalCode
  
  def setAddress(self):
    self.streetName = input("What is your street name? ")
    self.streetNum = input("What is your street number? ")
    self.city = input("What is your city? ")
    self.province = input("What is your province? ")
    self.postalCode = input("What is your postal code? ")
    return self
  
  def displayAddress(self):
    return f"Your address is {self.streetNum} {self.streetName} {self.city} {self.province} and your postal code is {self.postalCode}."

myhome = address().setAddress()

print(myhome.displayAddress())