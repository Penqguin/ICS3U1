sum = 0
past_num = 0
num = int(input("Enter a number "))

while num != past_num:
    past_num = num
    sum += num
    num = int(input("Enter a number "))
    
sum += num

print(sum)