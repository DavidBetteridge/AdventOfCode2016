import networkx as nx

def what(x, y, n):
  t = x*x + 3*x + 2*x*y + y + y*y
  t += n
  ones = bin(t).count("1")
  if ones % 2 == 1:
    return "#"
  else:
    return "."



n = 1352
target_x = 31
target_y = 39

directions = [(0,-1), (-1, 0), (1, 0), (0, 1)]

def find_route(rows, columns) -> bool:
  G = nx.DiGraph()
  for y in range(rows):
    for x in range(columns):
      if what(x, y, n) == ".":
        for x_offset, y_offset in directions:
          x2 = x + x_offset
          y2 = y + y_offset
          if x2 >= 0 and y2 >= 0:
            if what(x2, y2, n) == ".":
              G.add_edge((x, y), (x2,y2))

  try:
    return nx.dijkstra_path_length(G, (1,1), (target_x, target_y))
  except:
    return None

rows = target_y
columns = target_x
while (first_solution := find_route(rows, columns)) is None:
  rows += 1
  columns += 1

# Part 1
print(find_route(first_solution, first_solution))


G = nx.DiGraph()
for y in range(52):
  for x in range(52):
    if what(x, y, n) == ".":
      for x_offset, y_offset in directions:
        x2 = x + x_offset
        y2 = y + y_offset
        if x2 >= 0 and y2 >= 0:
          if what(x2, y2, n) == ".":
            G.add_edge((x, y), (x2,y2))


part2 = 0
for y in range(52):
  for x in range(52):
    if what(x, y, n) == ".":
      try:
        if nx.dijkstra_path_length(G, (1,1),(x,y)) <= 50:
          part2 += 1
      except:
        pass
print(part2)  # 135