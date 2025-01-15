import time
import random
import json
from prettytable import PrettyTable

class Spaceship:
  def __init__(self, name = None):
    self.health = 3
    self.name = name if name else 'guest'
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
    with open("high_scores.json", "r+") as file:
      try:
        data = json.load(file)
      except json.JSONDecodeError:
        data = []
      data.append({"name": player.name, "score": player.score})
      file.seek(0)
      json.dump(data, file)
      file.truncate()
    print("Score saved to high scores!")
  except Exception as e:
    print(f"Error saving score: {e}")

def display_leaderboard(player):
  print("\nLeaderboard:")
  try:
    with open("high_scores.json", "r") as file:
      data = json.load(file)
      scores = sorted(data, key=lambda x: x["score"], reverse=True)
      # Show top 5 scores
      for i, score in enumerate(scores[:5], start=1):
        print(f"{i}. {score['name']}: {score['score']}")
      # Find the current player's score and show their position
      current_player_score = next((score for score in scores if score["name"] == player.name), None)
      if current_player_score:
        current_player_position = scores.index(current_player_score) + 1
        print(f"\nYou are currently ranked {current_player_position} with a score of {current_player_score['score']}")
      else:
        print("\nYou don't have a score yet.")
  except Exception as e:
    print(f"Error reading high scores: {e}")

def asteroidGen():
  # Define the grid size
  grid_size = 8

  # Create an empty grid
  grid = [[False for _ in range(5)] for _ in range(grid_size)]

  # Choose a random starting point for the path
  start_x = random.randint(0, 4)
  start_y = 0
  grid[start_y][start_x] = True

  # Define the possible movements (up, down, left, right)
  movements = [(0, 1), (0, -1), (1, 0), (-1, 0)]

  # Perform DFS to generate the path
  def dfs(x, y):
    if y >= grid_size - 1:
      return
    for dx, dy in movements:
      new_x, new_y = x + dx, y + dy
      if 0 <= new_x < 5 and 0 <= new_y < grid_size and not grid[new_y][new_x]:
        grid[new_y][new_x] = True
        dfs(new_x, new_y)

  # Start the DFS from the starting point
  dfs(start_x, start_y)

  # Convert the grid to a list of asteroid positions
  asteroid_positions = []
  for y in range(grid_size):
    row = []
    for x in range(5):
      if not grid[y][x]:
        row.append(x)
    asteroid_positions.append(row)

  return asteroid_positions

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
    
def start_menu():
    table = PrettyTable()
    table.header = True
    table.field_names = ([" Asteroid Game "])
    table.add_row([""])
    table.add_row([" 1. Start Game "])
    table.add_row([" 2. Leaderboard "])
    table.add_row([" 3. Keybinds "])
    table.add_row([" 4. Exit "])
    table.add_row([""])
    print(table)
    print("Enter your choice:")
    choice = input()
    return choice

def show_keybinds():
  table = PrettyTable(align="c")
  table.header = True
  table.field_names = ([" Action ", " Keybinds "])
  table.add_row(["", ""])
  table.add_row([" Move Left ", " a, left, l "])
  table.add_row([" Move Right ", " d, right, r "])
  table.add_row([" Exit ", " q, quit, e, exit "])
  table.add_row(["", ""])
  print(table)

def slow_print(*args):
  text = ' '.join(map(str, args))
  delay = 0.03  # Speed up or slow down
  for char in text:
    print(char, end='', flush=True)
    time.sleep(delay)
  print('')

def game_loop(player):
  asteroids = []
  survivable_path = asteroidGen()
  turn = 0
  while True:
    a = start_menu()
    
    if a == "1":
      slow_print("\033[32mGame starting... \033[0m")
      break
    
    elif a == "2":
      display_leaderboard(player)
      slow_print("\033[32mPress Enter to return to the menu... \033[0m")
      input('')
          
    elif a == "3":
      show_keybinds()
      slow_print("\033[32mPress Enter to return to the menu... \033[0m")
      input('')
      
    elif a == "4":
      slow_print("\033[32mGoodbye! \033[0m")
      return
      
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
    if move == "a" or move == "left" or move == "l":
      player.move_left()
    elif move == "d" or move == "right" or move == "r":
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
  slow_print("Would you like to save your score? (y/n): ")
  save_option = input("").lower()
  if save_option == "y" or save_option == "yes":
    save_high_score(player)
  slow_print("Would you like to view the leaderboard? (y/n): ")
  l = input("").lower()
  if l == "y" or l == "yes":
    display_leaderboard(player)
    slow_print("\033[32mPress Enter to return to the menu... \033[0m")
    input('')
    
  player.health = 3
  
  game_loop(player)

def main():
  slow_print("\033[32mPress Enter to start... \033[0m")
  input('')
  player = Spaceship(input("Enter a username: "))
  
  game_loop(player)

main()
