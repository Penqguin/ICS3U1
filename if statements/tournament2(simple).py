count = 0
if input("Input W or L: ") == "W":
    count += 1
if input("Input W or L: ") == "W":
    count += 1
if input("Input W or L: ") == "W":
    count += 1
if input("Input W or L: ") == "W":
    count += 1
if input("Input W or L: ") == "W":
    count += 1
if count > 0:
    if count <= 2:
        print(3)
    elif count <= 4:
        print(2)
    else: 
        print(1)
else:
    print(-1)