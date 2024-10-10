max = 0
num = int(input("Enter a number: "))
while num != -1:
    if num > max:
        max = num
    print("Current max number is: ", max)
    num = int(input("Enter a number: "))
print(f"The highest number you entered was {max}")