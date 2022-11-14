import re
from typing import List

pattern = "^\/dev\/grid\/node-x(?P<x>[0-9]+)-y(?P<y>[0-9]+)\s+(?P<size>[0-9]+)T\s+(?P<used>[0-9]+)T\s+(?P<available>[0-9]+)T\s+(?P<use>[0-9]+)%"
def parse_line(line:str):
  match = re.match(pattern, line)
  return match.groupdict()

def read_file() -> List:
  with open("Day22/data.txt", "r") as f:
    lines = f.readlines()[2:]
  return [parse_line(line) for line in lines]

nodes = read_file()

minX = min(nodes, key=lambda d: int(d["x"]))["x"]
maxX = max(nodes, key=lambda d: int(d["x"]))["x"]
minY = min(nodes, key=lambda d: int(d["y"]))["y"]
maxY = max(nodes, key=lambda d: int(d["y"]))["y"]

total_pairs = 0
for node in nodes:
  for node2 in nodes:
    if node["x"] != node2["x"] or node["y"] != node2["y"]:
      if int(node["used"]) != 0:
        if int(node["used"]) <= int(node2["available"]):
          total_pairs+=1

print(total_pairs)

