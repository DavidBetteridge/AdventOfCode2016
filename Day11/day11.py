
from itertools import combinations
from typing import List


POLONIUM = 0b01
THULIUM = 0b10
PROMETHIUM = 0b100
RUTHENIUM = 0b1000
COBALT = 0b10000
NUMBER_OF_TYPES = 5

def generator(radioisotope):
  return radioisotope << NUMBER_OF_TYPES

def microchip(radioisotope):
  return radioisotope

def set_bit(value, bit):
  return value | (1<<bit)

def clear_bit(value, bit):
  return value & ~(1<<bit)

def testBit(int_type, offset):
  mask = 1 << offset
  return(int_type & mask)

def hash_state(current_floor: int, floor0: int, floor1: int, floor2: int, floor3: int):
  return current_floor \
          | (floor0 << 2) \
          | (floor1 << 2 + (2 * NUMBER_OF_TYPES)) \
          | (floor2 << 2 + (2 * NUMBER_OF_TYPES * 2)) \
          | (floor3 << 2 + (2 * NUMBER_OF_TYPES * 3))

def unhash_state(hashed_state: int):
  current_floor = hashed_state & 0b11
  floor0 = hashed_state & 0b1111111111 << 2
  floor1 = hashed_state & 0b1111111111 << 2 + (2 * NUMBER_OF_TYPES)
  floor2 = hashed_state & 0b1111111111 << 2 + (2 * NUMBER_OF_TYPES * 2)
  floor3 = hashed_state & 0b1111111111 << 2 + (2 * NUMBER_OF_TYPES * 3)
  return current_floor, [floor0, floor1, floor2, floor3]

# Initial state
floor3 = 0
floor2 = 0
floor1 = microchip(POLONIUM) | microchip(PROMETHIUM)
floor0 = generator(POLONIUM) | generator(THULIUM) | microchip(THULIUM) | \
         generator(PROMETHIUM) | generator(RUTHENIUM) | microchip(RUTHENIUM) | \
         generator(COBALT) | microchip(COBALT)
current_floor = 0
initial_state = hash_state(current_floor, floor0, floor1, floor2, floor3)

target = generator(POLONIUM) | microchip(POLONIUM) | \
         generator(THULIUM) | microchip(THULIUM) | \
         generator(PROMETHIUM) | microchip(PROMETHIUM) | \
         generator(RUTHENIUM) | microchip(RUTHENIUM) | \
         generator(COBALT) | microchip(COBALT)

def floor_is_valid(floor_contents:int):
  # If the floor contains at least one generator,  then all microchips must have their matching generators
  if (floor_contents >> NUMBER_OF_TYPES) == 0:
    return True  # No generators
  
  for i in range(NUMBER_OF_TYPES):
    if testBit(floor_contents, i) and not testBit(floor_contents, i + NUMBER_OF_TYPES):
      return False  # Microchip without a generator
  return True

def possible_moves(floor_no: int, floors: List[int]) -> List[int]:
  valid_moves = []
  positions = list(range(0, NUMBER_OF_TYPES * 2))
  current_floor = floors[floor_no]

  # Moving one at a time
  for to_move in positions:
    if current_floor & to_move:
      # Would this floor be valid without them?
      if floor_is_valid(clear_bit(current_floor, to_move)):
        if floor_no > 1:
          amended_floor = set_bit(floors[floor_no-1], to_move)
          if floor_is_valid(amended_floor):
            # Moving down is fine
            new_state = hash_state(floor_no-1, floors[0], floors[1], floors[2], floors[3])
            valid_moves.append(new_state)

        if floor_no < 3:
          amended_floor = set_bit(floors[floor_no+1], to_move)
          if floor_is_valid(amended_floor):
            # Moving up is fine
            new_state = hash_state(floor_no+1, floors[0], floors[1], floors[2], floors[3])
            valid_moves.append(new_state)

  return valid_moves

  # for to_move in combinations(positions, r=2):
  #   if current_floor & to_move[0]:
  #     pass
#     # Would this floor be valid without them?
#     amended_current_floor = remove_from_floor(current_floor_contents, to_move)
#     amended_current_floor_str = ".".join(amended_current_floor)
#     if floor_is_valid(amended_current_floor):

#       # Move down
#       if current_floor > 1:
#         lower_floor_contents: str = current_state.floor_contents(current_floor-1)
#         amended_lower_floor = add_to_floor(lower_floor_contents, to_move)
#         amended_lower_floor_str = ".".join(amended_lower_floor)
#         if floor_is_valid(amended_lower_floor):
#           new_state = state(current_floor-1,
#                             updated_floor_contents(current_state, 1, amended_current_floor_str, current_floor-1, amended_lower_floor_str),
#                             updated_floor_contents(current_state, 2, amended_current_floor_str, current_floor-1, amended_lower_floor_str),
#                             updated_floor_contents(current_state, 3, amended_current_floor_str, current_floor-1, amended_lower_floor_str),
#                             updated_floor_contents(current_state, 4, amended_current_floor_str, current_floor-1, amended_lower_floor_str),
#                             current_state.depth + 1)
#           valid_moves.append(new_state)
      
#       # Move up
#       if current_floor < 4:
#         upper_floor_contents: str = current_state.floor_contents(current_floor+1)
#         amended_upper_floor = add_to_floor(upper_floor_contents, to_move)
#         amended_upper_floor_str = ".".join(amended_upper_floor)
#         if floor_is_valid(amended_upper_floor):
#           new_state = state(current_floor+1,
#                             updated_floor_contents(current_state, 1, amended_current_floor_str, current_floor+1, amended_upper_floor_str),
#                             updated_floor_contents(current_state, 2, amended_current_floor_str, current_floor+1, amended_upper_floor_str),
#                             updated_floor_contents(current_state, 3, amended_current_floor_str, current_floor+1, amended_upper_floor_str),
#                             updated_floor_contents(current_state, 4, amended_current_floor_str, current_floor+1, amended_upper_floor_str),
#                             current_state.depth + 1)
#           valid_moves.append(new_state)
#   return valid_moves


best_depth = 99999
to_process = set([initial_state])
processed = set()
while len(to_process) > 0:
  next_state = to_process.pop()
  if next_state not in processed:
    processed.add(next_state)
    current_floor, floors = unhash_state(next_state)
    for move in possible_moves(current_floor, floors):
      if move.floor_4 == target:
        depth=min(best_depth,next_state.depth)
      elif move not in processed and move not in to_process:
        to_process.add(move)
  else:
    print("Cache hit")
print(depth)






# # The first floor contains a hydrogen-compatible microchip and a lithium-compatible microchip.
# # The second floor contains a hydrogen generator.
# # The third floor contains a lithium generator.
# # The fourth floor contains nothing relevant.
# from itertools import combinations
# from typing import List, Tuple
# from dataclasses import dataclass

# @dataclass(frozen=True, eq=True)
# class state:
#   floor_number: int
#   floor_1: str
#   floor_2: str
#   floor_3: str
#   floor_4: str
#   depth: int

#   def floor_contents(self, floor: int) -> str:
#     if floor == 1:
#       return self.floor_1
#     elif floor == 2:
#       return self.floor_2
#     elif floor == 3:
#       return self.floor_3
#     elif floor == 4:
#       return self.floor_4


# target = "CG.CM.LG.LM.PG.PM.RG.RM"
# # target = "CG.CM.LG.LM.PG.PM.RG.RM.TG.TM"
# # target = "CG.CM.DG.DM.EG.EM.LG.LM.PG.PM.RG.RM.TG.TM"

# initial_state = state(1,
#       "CG.CM.LG.PG.RG.RM",
#       # "CG.CM.LG.PG.RG.RM.TG.TM",
#       # "CG.CM.DG.DM.EG.EM.LG.PG.RG.RM.TG.TM",
#       "LM.PM",
#       "",
#       "",
#       0)

# def floor_is_valid(contents: List[str]):
#   G_count = len([content for content in contents if content.endswith("G") ])
#   for item in contents:
#     if item.endswith("M") and not f"{item[0]}G" in contents and G_count > 0:
#       return False
#   return True

# def combinations_of_items(floor_contents: Tuple[str,...]):
#   contents = floor_contents.split(".")

#   microchips = [thing[0] for thing in contents if thing.endswith("M")]
#   generators = [thing[0] for thing in contents if thing.endswith("G")]
#   pairs = [thing for thing in microchips if thing in generators]
#   worth_moving = set([m+'M' for m in microchips if m not in generators] + [g+'G' for g in generators if g not in microchips])
#   if len(pairs) > 0:
#     worth_moving.add(pairs[0]+'M')
#     worth_moving.add(pairs[0]+'G')
#   if len(pairs) > 1:
#     worth_moving.add(pairs[1]+'M')
#     worth_moving.add(pairs[1]+'G')

#   for to_move in worth_moving:
#     yield [to_move]
#   for to_move in combinations(worth_moving, r=2):
#     yield list(to_move)


# def remove_from_floor(current_contents: str, to_remove: Tuple[str,...]) -> List[str]:
#   if current_contents == "":
#     parts = []
#   else:
#     parts = current_contents.split(".")
#   for thing in to_remove:
#     parts.remove(thing)
#   return parts

# def add_to_floor(current_contents: str, to_add: Tuple[str,...]) -> List[str]:
#   if current_contents == "":
#     parts = []
#   else:
#     parts = current_contents.split(".")
#   for thing in to_add:
#     if thing!="":
#       parts.append(thing)
#   return sorted(parts)

# def updated_floor_contents(current_state: state,
#                            floor_to_process: int,
#                            amended_current_floor: str,
#                            amended_floor_number: int,
#                            amended_floor_content: str) -> str:
#   if floor_to_process == current_state.floor_number:
#     return amended_current_floor
#   elif floor_to_process == amended_floor_number:
#     return amended_floor_content
#   else:
#     return current_state.floor_contents(floor_to_process)

# def possible_moves(current_state: state) -> List:
#   current_floor = current_state.floor_number
#   current_floor_contents: str = current_state.floor_contents(current_floor)

#   valid_moves = []
#   for to_move in combinations_of_items(current_floor_contents):

#     # Would this floor be valid without them?
#     amended_current_floor = remove_from_floor(current_floor_contents, to_move)
#     amended_current_floor_str = ".".join(amended_current_floor)
#     if floor_is_valid(amended_current_floor):

#       # Move down
#       if current_floor > 1:
#         lower_floor_contents: str = current_state.floor_contents(current_floor-1)
#         amended_lower_floor = add_to_floor(lower_floor_contents, to_move)
#         amended_lower_floor_str = ".".join(amended_lower_floor)
#         if floor_is_valid(amended_lower_floor):
#           new_state = state(current_floor-1,
#                             updated_floor_contents(current_state, 1, amended_current_floor_str, current_floor-1, amended_lower_floor_str),
#                             updated_floor_contents(current_state, 2, amended_current_floor_str, current_floor-1, amended_lower_floor_str),
#                             updated_floor_contents(current_state, 3, amended_current_floor_str, current_floor-1, amended_lower_floor_str),
#                             updated_floor_contents(current_state, 4, amended_current_floor_str, current_floor-1, amended_lower_floor_str),
#                             current_state.depth + 1)
#           valid_moves.append(new_state)
      
#       # Move up
#       if current_floor < 4:
#         upper_floor_contents: str = current_state.floor_contents(current_floor+1)
#         amended_upper_floor = add_to_floor(upper_floor_contents, to_move)
#         amended_upper_floor_str = ".".join(amended_upper_floor)
#         if floor_is_valid(amended_upper_floor):
#           new_state = state(current_floor+1,
#                             updated_floor_contents(current_state, 1, amended_current_floor_str, current_floor+1, amended_upper_floor_str),
#                             updated_floor_contents(current_state, 2, amended_current_floor_str, current_floor+1, amended_upper_floor_str),
#                             updated_floor_contents(current_state, 3, amended_current_floor_str, current_floor+1, amended_upper_floor_str),
#                             updated_floor_contents(current_state, 4, amended_current_floor_str, current_floor+1, amended_upper_floor_str),
#                             current_state.depth + 1)
#           valid_moves.append(new_state)
#   return valid_moves

# depth = 99999
# to_process = set([initial_state])
# processed = set()
# while len(to_process) > 0:
#   next_state = to_process.pop()
#   if next_state not in processed:
#     processed.add(next_state)

#     for move in possible_moves(next_state):
#       if move.floor_4 == target:
#         depth=min(depth,next_state.depth)
#       elif move not in processed and move not in to_process:
#         to_process.add(move)
#   else:
#     print("Cache hit")
# print(depth)

# # RTG paired with corresponding chip
# # RTG is dangerous to other chips unless that chip is conected to it's own RTG
# # Lift must carry one or two items at a time
# # List only moves 1 floor at a time



# # to_process = []
# # processed = set()

# # to_process.append(json.dumps(initial_state))
# # G.add_node(json.dumps(initial_state))

# # def move(state, current_state, current_floor_number, move_to_floor_number, to_move, amended_floor):
# #     new_floor = copy_and_add(current_state[str(move_to_floor_number)], to_move)
# #     if floor_is_valid(new_floor):
# #       new_state = deepcopy(current_state)
# #       new_state["e"] = move_to_floor_number
# #       new_state[str(current_floor_number)] = amended_floor
# #       new_state[str(move_to_floor_number)] = new_floor
# #       new_state_json = json.dumps(new_state)
# #       G.add_edge(state, new_state_json)
# #       if new_state_json not in processed and new_state_json not in to_process:
# #         to_process.append(new_state_json)

# # while len(to_process) > 0:
# #   state = to_process.pop()
# #   if state not in processed:
# #     processed.add(state)

# #     current_state = json.loads(state)
# #     current_floor = int(current_state["e"])
# #     floor_contents: List[str] = current_state[str(current_floor)]

# #     for to_move in possible_moves(floor_contents):
# #       amended_floor = copy_and_remove(floor_contents, to_move)
# #       if floor_is_valid(amended_floor):
# #         if current_floor < 4:
# #           move(state, current_state,
# #                current_floor, current_floor+1, to_move, amended_floor)
            
# #         if current_floor > 1:
# #           move(state, current_state,
# #                 current_floor, current_floor-1, to_move, amended_floor)

# # print(G)              
# # route = (nx.dijkstra_path(G,
# #           source=json.dumps(initial_state),
# #           target=json.dumps(target_state)))
# # print(len(route)-1)  #47
# #22


