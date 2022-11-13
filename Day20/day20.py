
from typing import List, Tuple

def read_file() -> List[Tuple[int, int]]:
  def line_to_pair(line: str):
    from_, to_ = line.split("-")
    return (int(from_.strip()), int(to_.strip()))

  with open('Day20/data.txt') as f:
    lines = f.readlines()
    return [line_to_pair(line) for line in lines]


bag = read_file()

# Combine overlapping
combined = []
while len(bag) > 0:
  next = bag.pop()
  for other in bag:
    if other[0] <= next[1] and other[1] >= next[0]:
      bag.remove(other)
      bag.append((min(other[0], next[0]), max(other[1], next[1])))
      break
  else:
    combined.append(next)

# Combine adjacent ranges
in_order = sorted(combined)
i = 0
while i < len(in_order) - 1:
  if in_order[i][1]+1 == in_order[i+1][0]:
    a = in_order.pop(i)
    b = in_order.pop(i)
    in_order.insert(i, (a[0],b[1]))
  else:
    i+=1

lowest_gap = in_order[0][1]+1

print(lowest_gap)

