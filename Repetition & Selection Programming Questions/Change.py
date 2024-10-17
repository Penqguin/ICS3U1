#this code sucks
change = int(input("How much change? "))
while change <= 0  or change >=100:
    change = int(input("Enter an amout of change between 0 - 100"))
def quarters(change):
    quarters = change // 25
    return quarters
def dimes(change):
    dimes = (change - 25 * quarters(change)) // 10
    return dimes
def nickles(change):
    nickles = (change - (quarters(change) * 25) - (dimes(change) * 10)) // 5
    return nickles
def pennies(change):
    pennies = (change - (quarters(change) * 25) - (dimes(change) * 10) - (nickles(change) * 5))
    return pennies
print(quarters(change), "\n", dimes(change), "\n", nickles(change), "\n", pennies(change), "\n")