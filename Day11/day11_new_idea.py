from dataclasses import dataclass
from collections import deque
from typing import Deque, List, Set, Tuple
from functools import lru_cache

MICROCHIP = 0
GENERATOR = 1

@dataclass
class State:
  moves: int
  e: int
  items: List[Tuple[int,int]]  #M,G

SeenState = Tuple[int, ...]


def is_solution(state: State) -> bool:
  return all(m==4 and h==4 for m,h in state.items)

@lru_cache(maxsize=None)
def floor_is_valid(floor: int, items: Tuple[Tuple[int,int],...]) -> bool:
  has_generator = any([g == floor for _,g in items])
  if has_generator:
    has_chip_but_no_generator = any([c == floor and g != floor for c,g in items])
    if has_chip_but_no_generator:
      return False
  return True

def find_available_moves(state: State) -> List[State]:
  n_items = len(state.items)    # 0.... n-1
  possible_moves: List[List[Tuple[int,int]]] = []
  available_moves = []
  
  # Just microchips
  microchips = [ [(i,MICROCHIP)] for i in range(n_items) if state.items[i][MICROCHIP] == state.e]
  possible_moves += microchips

  # Just generators
  generators = [ [(i,GENERATOR)] for i in range(n_items) if state.items[i][GENERATOR] == state.e]
  possible_moves += generators

  
  # All pairs of moves.
  combinations = []
  for pair1 in possible_moves:
    for pair2 in possible_moves:
      if pair1[0] < pair2[0]:
        combinations.append([pair1[0],pair2[0]])
  possible_moves += combinations


  for dir in [-1, 1]:
    new_floor = state.e + dir
    if 1 <= new_floor <= 4:
      for possible_move in possible_moves:
        items = list(state.items)
        for item_type, chip_or_gen in possible_move:
          if chip_or_gen == MICROCHIP:
            items[item_type] = (new_floor,items[item_type][GENERATOR])
          else:
            items[item_type] = (items[item_type][MICROCHIP], new_floor)

        if floor_is_valid(state.e, tuple(items)) and floor_is_valid(new_floor, tuple(items)):
          available_moves.append(State(state.moves+1, new_floor, items))

  return available_moves

def state_to_seen_cache(state: State) -> Tuple[int, ...]:
  floors = [state.e]
  for floor in range(1,5):
    floor_items = []
    for (m,g) in state.items:
      if m == floor:
        floor_items.append(g)
    floors = floors + sorted(floor_items) + [-1]
  return tuple(floors)


queue: Deque[State] = deque()
seen: Set[SeenState] = set()

initial_state = State(0, 1, [(1,2), (1,3)])  #11
#initial_state = State(0, 1, [(1,1), (1,1), (1,1), (2,1), (2,1)])  #47
initial_state = State(0, 1, [(1,1), (1,1), (1,1), (1,1), (1,1), (2,1), (2,1)])  #71
queue.append(initial_state)

solution_found = False
while not solution_found:
  next = queue.popleft()
  available_moves = find_available_moves(next)
  for available_move in available_moves:
    cachable = state_to_seen_cache(available_move)
    if not cachable in seen:
      seen.add(cachable)
      if is_solution(available_move):
        solution_found = True
        print(available_move.moves)
      else:
        queue.append(available_move)
