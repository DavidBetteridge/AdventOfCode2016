def reverse_and_invert(a: str) -> str:
  b = ""
  for d in a:
    if d == "0":
      b = "1" + b
    else:
      b = "0" + b
  return b

def calculate_checksum(checksum: str) -> str:
  while len(checksum) % 2 == 0:
    new_checksum = ""
    for i in range(len(checksum))[::2]:
      if checksum[i] == checksum[i+1]:
        new_checksum += "1"
      else:
        new_checksum += "0"
    checksum = new_checksum
  return checksum

target_length=272
a = "10001001100000001"

while len(a) < target_length:
  b = reverse_and_invert(a)
  a = f"{a}0{b}"
a = a[:target_length]
print(a)
print(calculate_checksum(a))

