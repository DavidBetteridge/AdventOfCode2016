from collections import deque
from typing import Any, Deque, List, Set

State = Any
SeenState = Any


def is_solution(state: State) -> bool:
  return True

def find_available_moves(state: State) -> List[State]:
  return []

def state_to_seen_cache(state: State) -> SeenState:
  return state

queue: Deque[State] = deque()
seen: Set[SeenState] = set()

initial_state = "" #TODO: Add initial state
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
      else:
        queue.append(available_move)
