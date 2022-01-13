from typing import Optional, Tuple

with open('Day09/data.txt') as f:
  text = f.read().strip()

def read_int(text: str, start_from: int) -> Tuple[int, Optional[int]]:
  r = ""
  i = start_from
  while i < len(text) and text[i].isdigit():
    r += text[i]
    i += 1
  if r != "":
    return i, int(r)
  else:
    return i, None


def decompressed_length(text: str) -> int:
  i = 0
  length = 0
  while i < len(text):
    if text[i] == "(":
      i2, number_of_chrs = read_int(text, i+1)
      if number_of_chrs is not None and text[i2] == "x":
        i2, repeats = read_int(text, i2+1)
        if repeats is not None and text[i2] == ")":
          length += number_of_chrs * repeats
          i = i2+number_of_chrs+1
          continue
    length+=1
    i+=1
  return length


assert decompressed_length("ADVENT") == 6
assert decompressed_length("A(1x5)BC") == 7
assert decompressed_length("(3x3)XYZ") == 9
assert decompressed_length("A(2x2)BCD(2x2)EFG") == 11
assert decompressed_length("(6x1)(1x3)A") == 6
assert decompressed_length("X(8x2)(3x3)ABCY") == 18

print(decompressed_length(text))