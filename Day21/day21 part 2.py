import re
from typing import List

def swap_by_position(password: List[str], x: int, y: int) -> List[str]:
  temp = password[x]
  password[x] = password[y]
  password[y] = temp
  return password

def swap_letters(password: List[str], x: str, y: str) -> List[str]:
  return [ x if c == y else y if c == x else c for c in password]

def reverse_letters(password: List[str], x: int, y: int) -> List[str]:
  lhs = password[:x]
  middle = password[x:y+1][::-1]
  rhs = password[y+1:]
  return lhs + middle + rhs

def rotate_left(password: List[str], x: int) -> List[str]:
  x = x % len(password)
  rhs = password[:x]
  middle = password[x:]
  return middle + rhs

def rotate_right(password: List[str], x: int) -> List[str]:
  x = x % len(password)
  lhs = password[-x:]
  middle = password[:-x]
  return lhs + middle

def rotate_right_using_position(password: List[str], x: str) -> List[str]:
  pos = password.index(x) 
  if pos >= 4:
    pos+=1
  return rotate_right(password, pos + 1)

def undo_rotate_right_using_position(password: List[str], x: str) -> List[str]:
  mapping = {
    0: 1,
    1: 1,
    2: -2,
    3: 2,
    4: -1,
    5: 3,
    6: 0,
    7: 4,
  }
  pos = password.index(x) 

  return rotate_left(password, mapping[pos])

def move_by_position(password: List[str], x: int, y: int) -> List[str]:
  c = password.pop(x)
  password.insert(y, c)
  return password

def read_file() -> List[str]:
  with open("Day21/data.txt", "r") as f:
    lines = f.readlines()
    return lines



commands = read_file()
passcode = list("fbgdceah")

for command in commands[::-1]:
  command = command.strip()

  if (match := re.match('^swap position (?P<x>[0-9]) with position (?P<y>[0-9])$', command)):
    values = match.groupdict()
    passcode = swap_by_position(passcode, int(values["y"]), int(values["x"]))
    
  elif (match := re.match('^swap letter (?P<x>[a-z]) with letter (?P<y>[a-z])$', command)):
    values = match.groupdict()
    passcode = swap_letters(passcode, values["y"], values["x"])

  elif (match := re.match('^rotate based on position of letter (?P<x>[a-z])$', command)):
    values = match.groupdict()
    passcode = undo_rotate_right_using_position(passcode, values["x"])

  elif (match := re.match('^rotate right (?P<x>[0-9]) step[s]?$', command)):
    values = match.groupdict()
    passcode = rotate_left(passcode, int(values["x"]))

  elif (match := re.match('^rotate left (?P<x>[0-9]) step[s]?$', command)):
    values = match.groupdict()
    passcode = rotate_right(passcode, int(values["x"]))

  elif (match := re.match('^reverse positions (?P<x>[0-9]) through (?P<y>[0-9])$', command)):
    values = match.groupdict()
    passcode = reverse_letters(passcode, int(values["x"]), int(values["y"]))

  elif (match := re.match('^move position (?P<x>[0-9]) to position (?P<y>[0-9])$', command)):
    values = match.groupdict()
    passcode = move_by_position(passcode, int(values["y"]), int(values["x"]))

  else:
    raise Exception("Unknown command " + command)

print("".join(passcode))
