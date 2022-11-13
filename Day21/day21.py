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
  rhs = password[:x]
  middle = password[x:]
  return middle + rhs

def rotate_right(password: List[str], x: int) -> List[str]:
  lhs = password[-x:]
  middle = password[:x+1]
  return lhs + middle

as_list = list("abcde")
as_list = swap_by_position(as_list, 4, 0)
as_list = swap_letters(as_list, "d", "b")
as_list = reverse_letters(as_list, 0, 4)
as_list = rotate_left(as_list, 1)
as_list = rotate_right(as_list, 2)

print(as_list)
