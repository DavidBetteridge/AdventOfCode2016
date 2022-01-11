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


target_length=35651584
seed = "10001001100000001"

a_ = [seed]
b_ = [reverse_and_invert(a_[0])]

n = 0
while len(a_[n]) < target_length:
  n += 1
  b_.append(a_[n-1] + "1" + b_[n-1])
  a_.append(a_[n-1] + "0" + b_[n-1])
target2 = a_[n][:target_length]
print(len(target2))

print(calculate_checksum(target2))

