import re
from typing import Tuple
with open('Day03/data.txt') as f:
  triangles = [line.strip() for line in f.readlines()]


def is_valid(a: int, b: int, c: int) -> int:
  if ((a + b) > c) and ((a + c) > b) and ((b + c) > a):
    return 1
  else:
    return 0


def parse_triangle(triangle: str) -> Tuple[int,int,int]:
  a, b, c = re.split(r'\s+', triangle)
  return int(a), int(b), int(c)

# Part 1 - 917
print(sum(is_valid(*parse_triangle(triangle)) for triangle in triangles))

total = 0
for i in range(0, len(triangles), 3):
  triangle1 = parse_triangle(triangles[i])
  triangle2 = parse_triangle(triangles[i+1])
  triangle3 = parse_triangle(triangles[i+2])
  total += is_valid(triangle1[0],triangle2[0],triangle3[0])
  total += is_valid(triangle1[1],triangle2[1],triangle3[1])
  total += is_valid(triangle1[2],triangle2[2],triangle3[2])

# Part 2 - 1649
print(total)

