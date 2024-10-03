i = True
while i:
    try:
        a = int(input("What do you want to count down from: "))
    except ValueError or a <= 0:
        print("try again")
    else: 
        i = False
for i in range(1, 11):
    print(i)
for i in range(a, 0, -1):
    print(i)
print('times up!')