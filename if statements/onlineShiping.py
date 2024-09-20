onlineSpending = float(input("How much did you spending man :( : "))
bank = float(input("How much money you got: "))
bankAccount = bank - onlineSpending

if onlineSpending >= 100 and bankAccount > 100:
    print("Damn ur rich man")
elif bankAccount <= 100 and bankAccount > 10:
    print("At least you have some funds for food left")
elif bankAccount <= 10:
    print(";-;, and skill issue")
    print("** tip spend less money online")