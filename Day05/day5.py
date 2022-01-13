import hashlib

def part1():
  found = []
  current = 0
  door_id = "cxdnnyjw"
  m = hashlib.md5()
  while len(found) < 8:
    m.update((door_id+str(current)).encode('utf-8'))
    if m.hexdigest().startswith("00000"):
      found.append(m.hexdigest()[5])
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

part1()