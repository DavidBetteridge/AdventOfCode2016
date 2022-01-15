# The first floor contains a hydrogen-compatible microchip and a lithium-compatible microchip.
# The second floor contains a hydrogen generator.
# The third floor contains a lithium generator.
# The fourth floor contains nothing relevant.
import networkx as nx
import json
from copy import deepcopy
from typing import List
from itertools import combinations

def floor_is_valid(contents: List[str]):
  G_count = len([content for content in contents if content.endswith("G") ])
  for item in contents:
    if item.endswith("M") and not f"{item[0]}G" in contents and G_count > 0:
      return False
  return True


def copy_and_remove(contents: List[str], to_remove: List[str]) -> List[str]:
  return [content for content in contents if content not in to_remove]

def copy_and_add(contents: List[str], to_add: List[str]) -> List[str]:
  new_list = deepcopy(contents)
  for a in to_add:
    new_list.append(a)
  return sorted(new_list)

def possible_moves(floor_contents: List[str]):
  for to_move in combinations(floor_contents, r=1):
    yield to_move
  for to_move in combinations(floor_contents, r=2):
    yield to_move

G = nx.Graph()

initial_state = {
  "e":  1,
  1 : ["HM", "LM"],
  2 : ["HG"],
  3 : ["LG"],
  4 : [],
}

target_state = {
  "e":  4,
  1 : ["HG", "HM", "LG", "LM"],
  2 : [],
  3 : [],
  4 : [],
}

to_process = []
processed = set()

to_process.append(json.dumps(initial_state))
G.add_node(json.dumps(initial_state))

def move(state, current_state, current_floor_number, move_to_floor_number, to_move, amended_floor):
    new_floor = copy_and_add(current_state[str(move_to_floor_number)], to_move)
    if floor_is_valid(new_floor):
      new_state = deepcopy(current_state)
      new_state["e"] = move_to_floor_number
      new_state[str(current_floor_number)] = amended_floor
      new_state[str(move_to_floor_number)] = new_floor
      new_state_json = json.dumps(new_state)
      G.add_edge(state, new_state_json)
      if new_state_json not in processed:
        to_process.append(new_state_json)

while len(to_process) > 0:
  state = to_process.pop()
  if state not in processed:
    processed.add(state)

    current_state = json.loads(state)
    current_floor = int(current_state["e"])
    floor_contents: List[str] = current_state[str(current_floor)]

    for to_move in possible_moves(floor_contents):
      amended_floor = copy_and_remove(floor_contents, to_move)
      if floor_is_valid(amended_floor):
        if current_floor < 4:
          move(state, current_state,
               current_floor, current_floor+1, to_move, amended_floor)
            
        if current_floor > 1:
          move(state, current_state,
                current_floor, current_floor-1, to_move, amended_floor)


print(G)              
total, route = (nx.dijkstra_path(G,
          source=json.dumps(initial_state),
          target=json.dumps(target_state)))
print(route)
print(total)  #15358
