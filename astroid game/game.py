import time
import random

class spaceship():
  def __init__(self, name = 'guest'):
    self.health = 3
    self.name = name
    self.x_pos = 2
  
  def collision(self):
    self.health -= 1
    return self.health
  
  def gain_life(self):
    self.health +=1
    return self.health
  
  def move_left(self):
    self.x_pos -= 1
    return self.x_pos
  
  def move_right(self):
    self.x_pos += 1
    return self.x_pos

class asteroid():
  def __init__(self, x_pos, y_pos):
    self.health = 1
    self.x_pos = x_pos
    self.y_pos = y_pos

  def collision(self):
    self.health = 0
    return self.health

def check_collision(player, asteroids):
  for asteroid in asteroids:
    if player.x_pos == asteroid.x_pos:
      player.collision()
      asteroid.collision()
      print(f"You've hit an asteroid! \nlives remaining {player.health}")

# def update_score():

# def save_high_score():

def dfs():
  # generates new lines of asteroids and makes sure there is always an avalible path
  # path might not always be accessable to player to make game harder

def start():
  path = []
  current_pos = 0
  asteroids = []
  while True:
    path.append(current_pos)
    next_pos = random.randint(0, 4)
    while next_pos in path:
      next_pos = random.randint(0, 4)
    current_pos = next_pos
    if current_pos == 0:  # Reached the starting position, so the path is complete
      break
    # Add an asteroid at the current position
    asteroids.append(asteroid(current_pos, random.randint(0, 4)))
  return asteroids

def display_lanes(player, asteroids):
  # Update and display the current state of the lanes
  print(f"Player: {player.name}, Health: {player.health}, Position: {player.x_pos}")
  print("Lanes:")
  for i in range(5):
    if i == player.x_pos:
      print("^", end="")
    elif i in [asteroid.x_pos for asteroid in asteroids]:
      print("*", end="")
    else:
      print("-", end="")
    print(" ", end="")
  print()

#slow print function
def slow_print(*args):
    text = ' '.join(map(str, args))
    delay=0.03 #speed up or slow down
    for char in text:
       print(char, end='', flush=True)
       time.sleep(delay)
    print('')

def main():
  slow_print("Press any button to start... ")
  a = input('')

  player = spaceship(input("Enter a username"))
  asteroids = start()

  while a == a:
    display_lanes(player, asteroids)
    check_collision(player, asteroids)

main()