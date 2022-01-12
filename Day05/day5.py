import hashlib

def part1():
  found = []
  current = 0
  door_id = "cxdnnyjw"
  while len(found) < 8:
    if hashlib.md5((f"{door_id}{current}").encode()).hexdigest().startswith("00000"):
      found.append(hashlib.md5((f"{door_id}{current}").encode()).hexdigest()[5])
    current+=1
  print("".join(found))


def part2():
  found = [None]*8
  found_count = 0
  current = 0
  door_id = "cxdnnyjw"
  while found_count < 8:
    hash = hashlib.md5((f"{door_id}{current}").encode()).hexdigest()
    if hash.startswith("00000") and hash[5].isdigit():
      position = int(hash[5])
      if 0 <= position <= 7 and found[position] is None:
        found[position] = hash[6]
        found_count+=1
    current+=1

  print("".join(found))    