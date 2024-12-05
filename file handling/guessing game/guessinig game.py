import random

def game():
  ranNum = random.randint(1, 50)
  guess = int(input("Enter your guess: "))
  count = 0

  while guess != ranNum:
    count += 1
    if guess > ranNum:
      print("Guess a lower number")
    elif guess < ranNum:
      print("Guess a higher number")
    guess = int(input("Enter your guess: "))

  return count + 1

def updateScores(count):
  try:
    with open("file handling/guessing game/scores.txt", "r") as f:
      lines = f.readlines()
      highScore = float('inf')
      for line in lines:
        score = int(line.split('in ')[1].split(' guesses')[0])
        if score < highScore:
          highScore = score
      if count < highScore:
        with open("file handling/guessing game/scores.txt", "w") as f:
          f.write(f"You guessed the number in {count} guesses\n")
      else:
        with open("file handling/guessing game/scores.txt", "a") as f:
          f.write(f"You guessed the number in {count} guesses\n")
  except FileNotFoundError:
    with open("file handling/guessing game/scores.txt", "w") as f:
      f.write(f"You guessed the number in {count} guesses\n")

def getHighScore():
  try:
    with open("file handling/guessing game/scores.txt", "r") as f:
      highScore = float('inf')
      for line in f.readlines():
        score = int(line.split('in ')[1].split(' guesses')[0])
        if score < highScore:
          highScore = score
      return highScore
  except FileNotFoundError:
    return None

def main():
  print("Welcome to the Guessing Game!")
  print("You have to guess a number between 1 and 100")

  attempts = game()
  updateScores(attempts)
  highScore = getHighScore()

  if highScore is not None:
    print(f"Your score: {attempts} attempts")
    print(f"Current high score: {highScore} attempts")
  else:
    print(f"Your score: {attempts} attempts")
    print("No high score yet!")

if __name__ == '__main__':
  main()