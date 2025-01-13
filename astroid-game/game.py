import time
import random

class Spaceship:
  def __init__(self, name='guest'):
    self.health = 3
    self.name = name
    self.x_pos = 2  # Start in the middle lane
    self.score = 0
    self.streak = 0

  def collision(self):
    self.health -= 1
    self.streak = 0
    return self.health

  def gain_life(self):
    if self.health < 3:
      self.health += 1
    return self.health

  def move_left(self):
    if self.x_pos > 0:
      self.x_pos -= 1
    return self.x_pos

  def move_right(self):
    if self.x_pos < 4:
      self.x_pos += 1
    return self.x_pos


class Asteroid:
  def __init__(self, x_pos, y_pos):
    self.x_pos = x_pos
    self.y_pos = y_pos

  def move_down(self):
    self.y_pos += 1


def check_collision(player, asteroids):
  for asteroid in asteroids:
    if player.x_pos == asteroid.x_pos and asteroid.y_pos == 7:
      player.collision()
      print(f"You've hit an asteroid! Lives remaining: {player.health}")
      return True
  return False

def update_score(player, asteroids):
  dodged_asteroids = [asteroid for asteroid in asteroids if asteroid.y_pos > 7]
  if dodged_asteroids:
    player.score += len(dodged_asteroids)
    player.streak += len(dodged_asteroids)
    if player.streak >= 10:
      player.gain_life()
      print(f"Bonus! Lives increased to {player.health}")
      player.streak = 0


def save_high_score(player):
  try:
    with open("high_scores.txt", "a") as file:
      file.write(f"{player.name}: {player.score}\n")
    print("Score saved to high scores!")
  except Exception as e:
    print(f"Error saving score: {e}")

def asteroidGen():
  # generates asteroids
  path = []
  for _ in range(8):  # Generate 8 rows
    row_asteroids = []
    for _ in range(random.randint(0, 5)):  # Randomly generate 0-5 asteroids per row
      x_pos = random.randint(0, 4)  # Randomize the x-position of the asteroid
      row_asteroids.append(x_pos)
    path.append(row_asteroids)
  return path

def display_lanes(player, asteroids):
  # Create an empty 8x5 grid
  grid = [[" " for _ in range(5)] for _ in range(8)]

  # Place asteroids in the grid
  for asteroid in asteroids:
    if 0 <= asteroid.y_pos < 8:
      grid[asteroid.y_pos][asteroid.x_pos] = "*"

  # Place the player in the grid, overwriting any asteroid in the same lane
  grid[7][player.x_pos] = "^"

  # Display the grid with spacing between lanes
  print("\nCurrent Grid:")
  for row in grid:
    print("|", end="")
    for cell in row:
      if cell == "*":
        print(" \033[31m*\033[0m ", end="")  # Red color for asteroids
      elif cell == "^":
        if player.health >= 3:
          print(" \033[32m^\033[0m ", end="")  # Green color for player
        elif player.health == 2:
          print(" \033[33m^\033[0m ", end="")  # Yellow color for player
        elif player.health == 1:
          print(" \033[31m^\033[0m ", end="")  # Red color for player
        elif player.health == 0:
          print(" \033[31mX\033[0m ", end="")  # Red color for player
        
      else:
        print(f"   ", end="")  # Add a space between lanes
    print("|")  # End of row
  print(f"Player: {player.name}, Score: {player.score}, Lives: {player.health}")

def display_leaderboard():
  print("\nLeaderboard:")
  try:
    with open("high_scores.txt", "r") as file:
      scores = file.readlines()
      # clean and sort scores
      for score in scores:
        scores = [score.strip().split(":")]
      scores = [(name, int(points)) for name, points in scores if len(score) == 2 and points.isdigit()]
      
      # sort in descending order
      scores.sort(key=lambda x: x[1], reverse=True)
      
      if scores:
        for i, (name, points) in enumerate(scores, start=1):
          print(f"{i}. {name}: {points}")
      else:
        print("Leaderboard is empty.")
  except Exception as e:
    print(f"Error reading high scores: {e}")

def slow_print(*args):
  text = ' '.join(map(str, args))
  delay = 0.03  # Speed up or slow down
  for char in text:
    print(char, end='', flush=True)
    time.sleep(delay)
  print('')

def main():
  slow_print("\033[32mPress Enter to start... \033[0m")
  input('')
  player = Spaceship(input("Enter a username: "))
  asteroids = []
  survivable_path = asteroidGen()

  turn = 0
  while player.health > 0:
    print("\n" + "-" * 30)
    display_lanes(player, asteroids)

    # Move asteroids down and remove off-grid ones
    asteroids = [asteroid for asteroid in asteroids if asteroid.y_pos < 8]
    for asteroid in asteroids:
      asteroid.move_down()

    # Generate new asteroids
    if turn < len(survivable_path):
      for x_pos in survivable_path[turn]:
        asteroids.append(Asteroid(x_pos, 0))
    else:
      for _ in range(random.randint(0, 5)):  # Randomly generate 0-5 asteroids
        asteroids.append(Asteroid(random.randint(0, 4), 0))

    # Get player input
    move = input("Move (a: left, d: right, s: stay) or exit to quit: ").lower()
    if move == "a":
      player.move_left()
    elif move == "d":
      player.move_right()
    elif move == "exit" or move == "quit" or move == "q" or move == "e":
      break

    # Check for collisions and update score
    collision_occurred = check_collision(player, asteroids)
    if not collision_occurred:
      update_score(player, asteroids)

    turn += 1

  slow_print(f"\n\033[31mGame Over!\033[0m Score: {player.score}")
  display_lanes(player, asteroids)
  l = input("Would you like to view the leaderboard? (y/n): ").lower()
  if l == "y" or l == "yes":
    display_leaderboard()
  save_option = input("Would you like to save your score? (y/n): ").lower()
  if save_option == "y" or save_option == "yes":
    save_high_score(player)

main()
