import random

ans, guess, num = random.randint(1, 21), int(input("Enter a number between 1 and 20: ")), 0

while guess != ans:
    if guess > ans:
        print("Guess a lower number")
    elif guess < ans:
        print("Guess a higher number")
    guess = int(input("Enter a number between 1 and 20: "))
        
print(f"Great Job! You guessed the number!")