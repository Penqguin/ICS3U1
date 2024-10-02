m = int(input("number of months: "))
r = [float(input("amount of rainfall per month in mm: ")) for i in range(m)]
average = 0
for i in r:
    average += i
average /= m
print(average)