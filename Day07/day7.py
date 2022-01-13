from typing import Iterable, List, Tuple

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

def find_abas(list: List[str]) -> Iterable[str]:
  for section in list:
    for i in range(len(section)-2):
      if section[i] == section[i+2] and section[i] != section[i+1]:
        yield section[i:i+3]


def list_contains_abba(list: List[str]) -> bool:
  return any(contains_abba(section) for section in list)

def list_contains_bab(list: List[str], bab: str) -> bool:
  return any(bab in section for section in list)

def aba_to_bab(aba: str) -> str:
  return aba[1] + aba[0] + aba[1]

def address_supports_tls(address: str) -> bool:
  insides, outsides = split_address(address)    
  return list_contains_abba(outsides) and not list_contains_abba(insides)

def address_supports_ssl(address: str) -> bool:
  insides, outsides = split_address(address)   
  abas = find_abas(outsides)
  return any(list_contains_bab(insides, aba_to_bab(aba)) for aba in abas)

print(len([address for address in addresses if address_supports_tls(address)]))  #118

print(len([address for address in addresses if address_supports_ssl(address)]))  #260
