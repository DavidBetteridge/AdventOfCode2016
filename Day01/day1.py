from typing import List


def read_file() -> List[str]:
  with open('Day01/data.txt') as f:
    return f.read().strip().split(", ")

commands = read_file()

directions = ["N", "E", "S", "W"]
direction = 0
x = 0
y = 0

for command in commands:
  if command[0] == "R":
    direction = (direction + 1) % 4
  else:
    direction = (direction - 1) % 4

  if direction == 0:
    y += int(command[1:])
  elif direction == 2:
    y -= int(command[1:])    
  elif direction == 1:
    x += int(command[1:])    
  elif direction == 3:
    x -= int(command[1:])        

print(abs(x)+abs(y))  #291
