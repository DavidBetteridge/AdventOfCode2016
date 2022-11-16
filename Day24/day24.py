import networkx as nx
from itertools import permutations

def read_file():
  with open("day24/data.txt") as f:
    return [line.strip() for line in f.readlines()]


grid = read_file()

locations = {}
for row_number, row in enumerate(grid):
  for column_number, column in enumerate(row):
    if column.isnumeric():
      locations[column] = (column_number, row_number)


edges = []
for row_number, row in enumerate(grid):
  for column_number, column in enumerate(row):
    if column != '#':
      # Right
      if ((column_number+1) < len(row)) and (row[column_number+1] != '#'):
        from_ = (column_number, row_number)
        to_ = (column_number+1, row_number)
        edges.append((from_, to_))
      # Right
      if ((row_number+1) < len(grid)) and (grid[row_number+1][column_number] != '#'):
        from_ = (column_number, row_number)
        to_ = (column_number, row_number+1)
        edges.append((from_, to_))


G = nx.Graph()
G.add_edges_from(edges)
links = {}
for loc1 in locations:
  for loc2 in locations:
    if loc1 < loc2:
      l = len(nx.shortest_path(G, source=locations[loc1], target=locations[loc2]))
      links[(loc1, loc2)] = l-1
      links[(loc2, loc1)] = l-1


best = 99999
perms = permutations(["1", "2", "3", "4", "5", "6", "7"])
for perm in perms:
  total = links[("0", perm[0])]
  total += links[(perm[-1], "0")]  #part 2
  for i in range(0, 6):
    f = perm[i]
    t = perm[i+1]
    total += links[(f, t)]
  if total < best:
    best = total

print(best)