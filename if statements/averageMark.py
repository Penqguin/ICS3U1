f, s, l = map(float, input("Enter your 3 test scores: ").split())
average = (f + s + l) / 3
if average > 85:
    print("Congrats")
else:
    print("Study harder next time")