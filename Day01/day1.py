import numpy as np
from typing import List


def read_file() -> List[str]:
  with open('Day01/data.txt') as f:
    return f.read().strip().split(", ")

directions = [
  np.array([1,0]),   #North
  np.array([0,1]),   #East
  np.array([-1,0]),  #South
  np.array([0,-1]),  #West
  ]

commands = read_file()


def part1():
  current_direction = 0 #North
  position = np.array([0,0])      # X, Y

  for command in commands:
    if command[0] == "R":
      current_direction = (current_direction + 1) % 4
    else:
      current_direction = (current_direction - 1) % 4

    distance = int(command[1:])
    position = position + (distance * directions[current_direction])

  print(abs(position[0]) + abs(position[1]))


def part2():
  visited = set()
  current_direction = 0 #North
  position = np.array([0,0])      # X, Y

  for command in commands:
    if command[0] == "R":
      current_direction = (current_direction + 1) % 4
    else:
      current_direction = (current_direction - 1) % 4

    distance = int(command[1:])

    for _ in range(distance):
      position = position + directions[current_direction]
      if (position[0], position[1]) in visited:
        print(abs(position[0]) + abs(position[1]))
        return
      visited.add((position[0], position[1]))

  
part1()
part2()
  