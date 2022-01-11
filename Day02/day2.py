
current_number = 5

with open('Day02/data.txt') as f:
  instructions = [line.strip() for line in f.readlines()]

for instruction in instructions:
  for move in instruction:
    if move == "D" and current_number < 7:
        current_number += 3

    elif move == "U" and current_number > 3:
        current_number -= 3

    elif move == "R" and (current_number % 3 != 0):
        current_number += 1

    elif move == "L" and (current_number % 3 != 1):
        current_number -= 1      

  print(current_number)