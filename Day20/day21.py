
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


in_order = sorted(combined)

n_allowed = max(0, in_order[0][0]-1)   # Before first range
n_allowed += sum(in_order[i+1][0] - in_order[i][1] - 1
                 for i in range(len(in_order)-1))  # Gaps between ranges
n_allowed += 4294967295 - in_order[-1][1]  # After final range

assert n_allowed == 146
