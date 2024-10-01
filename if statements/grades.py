while True:
    try:
        grade = int(input("Grade: "))
    except ValueError:
        print("Enter a number")
    else:
        break

if grade <= 25:
    print("F")
elif grade <= 45:
    print("E")
elif grade <= 50:
    print("D")
elif grade <= 60:
    print("C")
elif grade <= 80:
    print("B")
else:
    print("A")