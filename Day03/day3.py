import re
from typing import Tuple
with open('Day03/data.txt') as f:
  triangles = [line.strip() for line in f.readlines()]


def is_valid(a: int, b: int, c: int) -> bool:
  return ((a + b) > c) and ((a + c) > b) and ((b + c) > a)

def parse_triangle(triangle: str) -> Tuple[int,int,int]:
  a, b, c = re.split(r'\s+', triangle)
  return int(a), int(b), int(c)

result = len([1 for triangle in triangles
              if is_valid(*parse_triangle(triangle))])
print(result)

