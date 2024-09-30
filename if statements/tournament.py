a = [input() for a in range(0, 6)].count("W")

if a > 0: 
    if a <= 2: 
        print(3)
    elif a <= 4: 
        print(2)
    else: 
        print(1)
else: 
    print(-1)