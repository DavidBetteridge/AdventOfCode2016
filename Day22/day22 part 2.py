import re
from dataclasses import dataclass
from typing import List

@dataclass
class Node:
  x: int
  y: int 
  size: int
  used: int
  available: int

pattern = "^\/dev\/grid\/node-x(?P<x>[0-9]+)-y(?P<y>[0-9]+)\s+(?P<size>[0-9]+)T\s+(?P<used>[0-9]+)T\s+(?P<available>[0-9]+)T\s+(?P<use>[0-9]+)%"
def parse_line(line:str):
  match = re.match(pattern, line)
  values = match.groupdict()
  return Node(int(values["x"]), int(values["y"]), int(values["size"]), int(values["used"]), int(values["available"]))

def read_file() -> List:
  with open("Day22/data.txt", "r") as f:
    lines = f.readlines()[2:]
  return [parse_line(line) for line in lines]

def swap_nodes(node1: Node, node2: Node):
  if node1.available < node2.used:
    raise Exception("Not enough space")
  size = node1.size
  used = node1.used
  available = node1.available
  node1.size = node2.size
  node1.used = node2.used
  node1.available = node2.available
  node2.size = size
  node2.used = used
  node2.available = available

nodes = read_file()

minX = min(nodes, key=lambda d: d.x).x
maxX = max(nodes, key=lambda d: d.x).x
minY = min(nodes, key=lambda d: d.y).y

nodes_by_x_y = {(node.x, node.y):node for node in nodes}

n_nodes = len(nodes_by_x_y)

goal = nodes_by_x_y[(maxX,minY)]

empty = [node for node in nodes if node.used == 0][0]

blockages = [node for node in nodes if node.size > 100]

moves = 0

# Far left
while (empty.x) > 0:
  node = nodes_by_x_y[(empty.x-1, empty.y)]
  swap_nodes(empty, node)
  empty=node
  moves+=1

# Top row
while (empty.y) > 0:
  node = nodes_by_x_y[(empty.x, empty.y-1)]
  swap_nodes(empty, node)
  empty=node
  moves+=1

# Stop just to the left of the goal
while (empty.x) < (maxX - 1):
  node = nodes_by_x_y[(empty.x+1, empty.y)]
  swap_nodes(empty, node)
  empty=node
  moves+=1

while goal.x > 1:
  swap_nodes(empty, goal)
  (empty,goal) = (goal, empty)
  moves+=1

  #Down
  node = nodes_by_x_y[(empty.x, empty.y+1)]
  swap_nodes(empty, node)
  empty=node
  moves+=1

  #Left x 2
  for _ in range(2):
    node = nodes_by_x_y[(empty.x-1, empty.y)]
    swap_nodes(empty, node)
    empty=node
    moves+=1  

  #Up
  node = nodes_by_x_y[(empty.x, empty.y-1)]
  swap_nodes(empty, node)
  empty=node
  moves+=1

swap_nodes(empty, goal)
(empty,goal) = (goal, empty)
moves+=1

print(moves)
