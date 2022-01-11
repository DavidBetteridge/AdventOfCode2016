from dataclasses import dataclass
from collections import deque
from typing import Deque, List, Set, Tuple
from functools import lru_cache
import time

MICROCHIP = 0
GENERATOR = 1

@dataclass
class State:
  moves: int
  e: int
  items: List[Tuple[int,int]]  #M,G

SeenState = Tuple[int, ...]

initial_state = State(0, 1, [(1,2), (1,3)])  #11
#initial_state = State(0, 1, [(1,1), (1,1), (1,1), (2,1), (2,1)])  #47
initial_state = State(0, 1, [(1,1), (1,1), (1,1), (1,1), (1,1), (2,1), (2,1)])  #71s


@lru_cache(maxsize=None)
def floor_is_valid(floor: int, items: Tuple[Tuple[int,int],...]) -> bool:
  has_generator = any([g == floor for _,g in items])
  if has_generator:
    has_chip_but_no_generator = any([c == floor and g != floor for c,g in items])
    if has_chip_but_no_generator:
      return False
  return True

def find_available_moves(state: State, seen: set, queue) -> bool:
  
  # Just microchips
  possible_moves = [ [(i,MICROCHIP)] for i in range(len(state.items)) if state.items[i][MICROCHIP] == state.e]

  # Just generators
  generators = [ [(i,GENERATOR)] for i in range(len(state.items)) if state.items[i][GENERATOR] == state.e]
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

        items_t = tuple(items)
        if floor_is_valid(state.e, items_t) and floor_is_valid(new_floor, items_t):
          available_move = State(state.moves+1, new_floor, items)
          cachable = state_to_seen_cache(available_move)
          if not cachable in seen:
            seen.add(cachable)
            queue.append(available_move)
            if is_solution(available_move):
              print(available_move.moves)
              return True

  return False

def is_solution(state: State) -> bool:
  return all(m==4 and h==4 for m,h in state.items)

def state_to_seen_cache(state: State) -> Tuple[int, ...]:
  floors = [g+(16*floor) for floor in range(1,5)
                         for (m,g) in state.items if m == floor]
  floors.append(state.e)
  return tuple(sorted(floors))

st = time.time()

queue: Deque[State] = deque()
seen: Set[SeenState] = set()
queue.append(initial_state)

solution_found = False
while not solution_found:
  next = queue.popleft()
  solution_found = find_available_moves(next, seen, queue)

elapsed_time = time.time() - st
print('Time taken:', elapsed_time, 'seconds')