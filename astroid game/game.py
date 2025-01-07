class spaceship():
  def __init__(self, name = 'guest'):
    self.health = 3
    self.name = name
    self.x_pos = 3
  
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

def check_collision(player):

def update_score():

def save_high_score():

def dfs():

def display_lanes(player):

def main():
  a = input("Press any button to start: ")

  player = spaceship(input("Enter a username"))

  while a == a:
    display_lanes(player)
    check_collision(player)
main()