num_of_side_lengths = int(input("Input the number of side lengths: "))
side_lengths = [float(input("input your side length: ")) for _ in range(num_of_side_lengths)]
perimeter = 0

for i in range(num_of_side_lengths):
    perimeter += side_lengths[i]
print("Perimeter is:", perimeter)