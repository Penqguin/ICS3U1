make, model, colour = map(str, input("What is the make, model and colour of your car? ").split())
year = int(input("What is the year? "))
if make == "honda" and model == "civic" and (colour == "black" or colour == "silver") and year >= 2015:
    print("BUY THE CAR")
else:
    print("DON'T BUY THE CAR")