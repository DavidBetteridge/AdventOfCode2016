from collections import defaultdict
from typing import List

def int_split(text: str, sep: str) -> List[int]:
  return[int(r) for r in text.split(sep)]



with open('Day08/data.txt') as f:
  commands = [line.strip() for line in f.readlines()]

NUMBER_OF_ROWS = 6
NUMBER_OF_COLUMNS = 50

grid = defaultdict(bool)

def print_row(grid, row):
  l=""
  for c in range(NUMBER_OF_COLUMNS):
    l+= "." if not grid[(c,row)] else '#'
  print(l)

def print_grid(grid):
  for r in range(NUMBER_OF_ROWS):
    print_row(grid, r)  


for command in commands:

  if command.startswith("rect"):
    parameters = command[5:]
    columns, rows = int_split(parameters,"x")
    
    for r in range(rows):
      for c in range(columns):
        grid[(c,r)] = True

  elif command.startswith("rotate row y="):
      parameters = command[len("rotate row y="):]
      row_number, distance = int_split(parameters," by ")
      
      for _ in range(distance):
        rhs = grid[(NUMBER_OF_COLUMNS-1,row_number)]
        for column_number in range(NUMBER_OF_COLUMNS,0,-1):
           grid[(column_number,row_number)] = grid[(column_number-1,row_number)]
        grid[(0,row_number)] = rhs


  elif command.startswith("rotate column x="):
      parameters = command[len("rotate column x="):]
      column_number, distance = int_split(parameters," by ")
      
      for _ in range(distance):
        rhs = grid[(column_number, NUMBER_OF_ROWS-1)]
        for row_number in range(NUMBER_OF_ROWS,0,-1):
           grid[(column_number,row_number)] = grid[(column_number,row_number-1)]
        grid[(column_number, 0)] = rhs
  else:
    raise Exception("Unknown command")


result = 0
for r in range(NUMBER_OF_ROWS):
  for c in range(NUMBER_OF_COLUMNS):
    if grid[(c,r)]:
      result += 1
print(result) 

print_grid(grid)