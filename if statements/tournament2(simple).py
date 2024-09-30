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
        print(1)
    elif count <= 4:
        print(2)
    else: 
        print(3)
else:
    print(-1)