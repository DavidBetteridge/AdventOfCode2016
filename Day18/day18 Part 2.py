puzzle_data = ".^^^.^.^^^.^.......^^.^^^^.^^^^..^^^^^.^.^^^..^^.^.^^..^.^..^^...^.^^.^^^...^^.^.^^^..^^^^.....^...."


def create_new_row(previous_row: str) -> str:
  previous_row =  f".{previous_row}."
  new_row = ""
  for i in range(1, len(puzzle_data)+1):
    previous = previous_row[i-1:i+2]
    if previous in ["..^","^..",".^^","^^."]:
      new_row += '^'
    else:
      new_row += '.'
  return new_row

row = puzzle_data
safe = 0
for _ in range(400000):
  safe += row.count(".")
  row = create_new_row(row)

print(safe)