from hashlib import md5
from typing import List, Tuple
from dataclasses import dataclass

Location = Tuple[int,int]

@dataclass(frozen=True)
class State:
  passcode: str
  route: str
  location: Location


def is_open(symbol: str) -> bool:
  return symbol in ["b","c", "d", "e", "f"]

def open_doors(passcode: str) -> List[bool]:
  doors = md5(passcode.encode()).hexdigest()[:4]
  return [is_open(s) for s in doors]

def available_options(passcode: str, location: Location) -> List:
  options = []
  possible_open_doors = open_doors(passcode)
  if location[1] > 0 and possible_open_doors[0]:
    options.append("U")

  if location[1] < 3 and possible_open_doors[1]:
    options.append("D")
  
  if location[0] > 0 and possible_open_doors[2]:
    options.append("L")

  if location[0] < 3 and possible_open_doors[3]:
    options.append("R")

  return options


location: Location = (0,0)
passcode = "bwnlcvfs"
stack = [State(passcode, "", location)]

shortest_solution = ""
longest_solution = ""

while len(stack) > 0:
  state = stack.pop()
  if state.location == (3,3):
    if shortest_solution == "" or len(shortest_solution) > len(state.route):
      shortest_solution = state.route
    if longest_solution == "" or len(longest_solution) < len(state.route):
      longest_solution = state.route      
  else:
    options = available_options(state.passcode, state.location)
    for option in options:
      if option == "R":
        new_location = (state.location[0]+1,state.location[1])
      elif option == "L": 
        new_location = (state.location[0]-1,state.location[1])
      elif option == "U": 
        new_location = (state.location[0],state.location[1]-1)
      elif option == "D": 
        new_location = (state.location[0],state.location[1]+1)

      stack.append(State(state.passcode+option, state.route+option, new_location))

print(shortest_solution)
print(len(longest_solution))
