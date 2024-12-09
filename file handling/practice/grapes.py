f = open("file handling/practice/grapes.txt", "r")
file = f.read()

for line in file.split("\n"):
  p = line.split(" ")
  print(f'{p[0]} \n{p[1]}')
