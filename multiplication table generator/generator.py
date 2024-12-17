"""
  Program to create a multiplication table from a user input
"""
def table(n):
  arr = []
  
  for i in range(1, 11):
    arr.append(f'{n} * {i} = {n*i}')
  return arr

def main():
  num = int(input('Enter a number: '))
  confirmation = str.lower(input(f'Do you want to make a table using {num}? enter (Y)es: '))

  if confirmation == 'y' or confirmation == 'yes':
    result = table(num)

    for i in result:
      print(i)
    
    confirmation = str.lower(input('Would you like to make another (Y)es or (N)o: '))

    if confirmation == 'y' or confirmation == 'yes':
      main()

main()