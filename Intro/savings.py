discount = float(input("Enter the discount(in decimal form): "))

original = float(input("What is the original price: "))
savings = discount * original
discountedPrice = original - savings

print("%.2f" % discountedPrice)