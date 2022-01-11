from typing import List


def read_file() -> List[str]:
  with open('Day01/data.txt') as f:
    return f.read().strip().split(", ")

commands = read_file()

directions = ["N", "E", "S", "W"]
direction = 0
x = 0
y = 0

visited = set()

for command in commands:
  if command[0] == "R":
    direction = (direction + 1) % 4
  else:
    direction = (direction - 1) % 4

  distance = int(command[1:])

  if direction == 0:
    for _ in range(distance):
      y += 1
      if (x,y) in visited:
        print(abs(x)+abs(y))
      else:
        visited.add((x,y))

  elif direction == 2:
    for _ in range(distance):
      y -= 1
      if (x,y) in visited:
        print(abs(x)+abs(y))
      else:
        visited.add((x,y))

  elif direction == 1:
    for _ in range(distance):
      x += 1
      if (x,y) in visited:
        print(abs(x)+abs(y))
      else:
        visited.add((x,y))

  elif direction == 3:
    for _ in range(distance):
      x -= 1
      if (x,y) in visited:
        print(abs(x)+abs(y))
      else:
        visited.add((x,y))       


