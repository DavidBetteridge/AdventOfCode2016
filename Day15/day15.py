# Disc #1 has 13 positions; at time=0, it is at position 1.
# Disc #2 has 19 positions; at time=0, it is at position 10.
# Disc #3 has 3 positions; at time=0, it is at position 2.
# Disc #4 has 7 positions; at time=0, it is at position 1.
# Disc #5 has 5 positions; at time=0, it is at position 3.
# Disc #6 has 17 positions; at time=0, it is at position 5.

start_time = 0
while True:
  start_time+=1
  disk1 = (1 + start_time) % 13
  if disk1 != 0:
    continue

  disk2 = (10 + start_time + 1) % 19
  if disk2 != 0:
    continue

  disk3 = (2 + start_time + 2) % 3
  if disk3 != 0:
    continue

  disk4 = (1 + start_time + 3) % 7
  if disk4 != 0:
    continue

  disk5 = (3 + start_time + 4) % 5
  if disk5 != 0:
    continue

  disk6 = (5 + start_time + 5) % 17
  if disk6 != 0:
    continue

  print(start_time-1)
  break
