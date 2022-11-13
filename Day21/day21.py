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


def move_by_position(password: List[str], x: int, y: int) -> List[str]:
  c = password.pop(x)
  password.insert(y, c)
  return password

as_list = list("abcde")
as_list = swap_by_position(as_list, 4, 0)
as_list = swap_letters(as_list, "d", "b")
as_list = reverse_letters(as_list, 0, 4)
as_list = rotate_left(as_list, 1)
as_list = move_by_position(as_list, 1, 4)
as_list = move_by_position(as_list, 3, 0)
as_list = rotate_right_using_position(as_list, "b")
as_list = rotate_right_using_position(as_list, "d")

print(as_list)
