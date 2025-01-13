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


def dfs():
  # Ensures there is at least one survivable path for the asteroids
  path = []
  while len(path) < 8:  # Generate 8 rows
    next_lane = random.randint(0, 4)
    path.append(next_lane)
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

    # Display the grid with fixed-width lanes
    print("\nCurrent Grid:")
    for row in grid:
        print("|", end="")
        for cell in row:
            print(f" {cell} |")  # Each lane is 3 characters wide (" |")
        print("~" * 16)  # Add a border below each row

    print(f"Player: {player.name}, Lives: {player.health}")




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
  survivable_path = dfs()

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
      asteroids.append(Asteroid(survivable_path[turn], 0))
    else:
      asteroids.append(Asteroid(random.randint(0, 4), 0))

    # Get player input
    move = input("Move (a: left, d: right, s: stay): ").lower()
    if move == "a":
      player.move_left()
    elif move == "d":
      player.move_right()
    elif move == "exit":
      break

    # Check for collisions and update score
    collision_occurred = check_collision(player, asteroids)
    if not collision_occurred:
      update_score(player, asteroids)

    turn += 1

  print(f"\nGame Over! Final Score: {player.score}")
  save_option = input("Would you like to save your score? (y/n): ").lower()
  if save_option == "y":
    save_high_score(player)

main()
