num = int(input("enter a number from 1 - 3: \n")) 

if num == 1:
    a = int(input("what is 3 * 3: \n"))
    if a == 9:
        print("You got it correct! Good job!")
    else:
        print("Sorry, wrong answer.")
elif num == 2:
    a = int((input("What is 4^2: \n")))
    if a == 16:
        print("You got it correct! Good job!")
    else:
        print("Sorry, wrong answer.")
elif num == 3:
    a = int((input("What is 4 * 10 / 2: \n")))
    if a == 20:
        print("You got it correct! Good job!")
    else:
        print("Sorry, wrong answer.")
else:
    print("you did not input a number that is associated with a question try again.")