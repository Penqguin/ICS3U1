a, b, c = map(int, input("Enter 3 ages? ").split())
eldest, middle, yongest = 0, 0, 0
if a >= b and a >= c:
    eldest = a
    if b >= c:
        yongest = c
        middle = b
    elif c >= b:
        yongest = b
        middle = c
elif b >= a and b >= c:
    eldest = b
    if a >= c:
        yongest = c
        middle = a
    elif c >= a:
        yongest = a
        middle = c
elif c >= a and c >= b:
    eldest = c
    if b >= a:
        yongest = a
        middle = b
    elif a >= b:
        yongest = b
        middle = a

print(eldest, middle, yongest)