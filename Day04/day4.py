import re
from collections import Counter

def is_real_room(room_details: str) -> int:
  encrypted_name, rest = re.split("[0-9]+",room_details)
  clean_encrypted_name = encrypted_name.replace("-","")
  letter_count = Counter(clean_encrypted_name)
  new_list = sorted(letter_count.items(), key=lambda a: (-a[1],a[0]))[:5]
  calculated_checksum = "".join([a[0] for a in new_list])
  clean_checksum = rest[1:-1]
  if clean_checksum == calculated_checksum:
    return int(room_details.split("[")[0].split("-")[-1])
  else:
    return 0

with open('Day04/data.txt') as f:
  rooms = [line.strip() for line in f.readlines()]

print(sum(is_real_room(room) for room in rooms))

