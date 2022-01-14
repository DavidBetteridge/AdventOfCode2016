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


def decompressed_length(text: str, fn) -> int:
  i = 0
  length = 0
  while i < len(text):
    if text[i] == "(":
      i2, number_of_chrs = read_int(text, i+1)
      if number_of_chrs is not None and text[i2] == "x":
        i2, repeats = read_int(text, i2+1)
        if repeats is not None and text[i2] == ")":
          length += repeats * fn(text[i2+1:i2+1+number_of_chrs], fn)
          i = i2+number_of_chrs+1
          continue
    length+=1
    i+=1
  return length


# Part 1
def string_len(text: str, fn) -> int:
  return len(text)
  
assert decompressed_length("ADVENT", string_len) == 6
assert decompressed_length("A(1x5)BC", string_len) == 7
assert decompressed_length("(3x3)XYZ", string_len) == 9
assert decompressed_length("A(2x2)BCD(2x2)EFG", string_len) == 11
assert decompressed_length("(6x1)(1x3)A", string_len) == 6
assert decompressed_length("X(8x2)(3x3)ABCY", string_len) == 18
print(decompressed_length(text, string_len))  #150914


# Part 2
assert decompressed_length("(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN", decompressed_length) == 445
print(decompressed_length(text, decompressed_length))  #11052855125