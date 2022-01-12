import hashlib

found = []
current = 0
door_id = "cxdnnyjw"
while len(found) < 8:
  if hashlib.md5((f"{door_id}{current}").encode()).hexdigest().startswith("00000"):
    found.append(hashlib.md5((f"{door_id}{current}").encode()).hexdigest()[5])
  current+=1

print("".join(found))    