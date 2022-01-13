from typing import List, Tuple


def split_address(address: str) -> Tuple[List[str], List[str]]:
  outsides = []
  insides = []
  
  close = -1
  open = address.find("[")
  while open >= 0:
    outsides.append(address[close+1:open])
    close = address.index("]", open)
    insides.append(address[open+1: close])
    open = address.find("[", close)

  if close+1 < len(address):
    outsides.append(address[close+1:])

  return insides, outsides


print(split_address("abba[mnop]qrst"))    
print(split_address("abba[mnop]qrst[a]"))    
