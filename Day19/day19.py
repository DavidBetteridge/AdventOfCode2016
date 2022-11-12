
elfs = [a for a in range(1, 3017957+1)]
while len(elfs) > 1:
  even = len(elfs) % 2 == 0
  elfs = [a for a in elfs[::2]]
  if not even:
    elfs = elfs[1:]
  print(elfs)

#1841611