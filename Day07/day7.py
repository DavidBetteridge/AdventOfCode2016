from typing import List, Tuple

with open('Day07/data.txt') as f:
  addresses = [line.strip() for line in f.readlines()]

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

def contains_abba(section: str) -> bool:
  for i in range(len(section)-3):
    if section[i] == section[i+3] and section[i+1] == section[i+2] and section[i] != section[i+1]:
      return True
  return False

def list_contains_abba(list: List[str]) -> bool:
  return any(contains_abba(section) for section in list)


def address_is_valid(address: str) -> bool:
  insides, outsides = split_address(address)    
  return list_contains_abba(outsides) and not list_contains_abba(insides)

print(len([address for address in addresses if address_is_valid(address)]))  #118