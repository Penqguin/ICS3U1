num = str(input("Input binary to convert to decimal: "))
while len(num) <= 0 or len(num) > 8:
    num = str(input("Input binary to convert to decimal: "))

def binaryToDecimal(binary):
    decimal, i = 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    print(decimal)

binaryToDecimal(int(num))#hi