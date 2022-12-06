
from itertools import combinations
from typing import Iterable, List


# HYDROGEN = 0b01
# LITHIUM = 0b10
# NUMBER_OF_TYPES = 2


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

def test_bit(int_type, offset):
  mask = 1 << offset
  return (int_type & mask) == mask

def set_floor_bits(state, floor_no):
  temp = clear_bit(state, 1)
  temp = clear_bit(temp, 0)
  return temp | floor_no

def bit_offset(floor_no):
  return (2 + (2 * NUMBER_OF_TYPES * floor_no))

def test_item_bits(state, floor_no, offsets: Iterable[int]):
  for offset in offsets:
    if not test_bit(state, bit_offset(floor_no) + offset):
      return False
  return True

def clear_item_bits(state, floor_no, offsets: Iterable[int]):
  for offset in offsets:
    state = clear_bit(state, bit_offset(floor_no) + offset)
  return state

def set_item_bits(state, floor_no, offsets: Iterable[int]):
  for offset in offsets:
    state = set_bit(state, bit_offset(floor_no) + offset)
  return state

def hash_state(current_floor: int, floor0: int, floor1: int, floor2: int, floor3: int):
  return current_floor \
          | (floor0 << 2) \
          | (floor1 << 2 + (2 * NUMBER_OF_TYPES)) \
          | (floor2 << 2 + (2 * NUMBER_OF_TYPES * 2)) \
          | (floor3 << 2 + (2 * NUMBER_OF_TYPES * 3))


def display(state: int):
  floor_no = state & 0b11

  for f in range(3, -1, -1):
    print(f"F{f} ", end="")
    if floor_no == f:
      print(f"E ", end="")
    else:
      print(f". ", end="")

    if test_bit(state, bit_offset(f) + 2):
      print(f"HG ", end="")
    else:
      print(f"   ", end="")  

    if test_bit(state, bit_offset(f) + 0):
      print(f"HM ", end="")
    else:
      print(f"   ", end="")           

    if test_bit(state, bit_offset(f) + 3):
      print(f"LG ", end="")
    else:
      print(f"   ", end="")

    if test_bit(state, bit_offset(f) + 1):
      print(f"LM ", end="")
    else:
      print(f"   ", end="")

    print("")
  print("")

# Initial state
floor3 = 0
floor2 = 0
floor1 = microchip(POLONIUM) | microchip(PROMETHIUM)
floor0 = generator(POLONIUM) | generator(THULIUM) | microchip(THULIUM) | \
         generator(PROMETHIUM) | generator(RUTHENIUM) | microchip(RUTHENIUM) | \
         generator(COBALT) | microchip(COBALT)

# floor3 = 0
# floor2 = generator(LITHIUM)
# floor1 = generator (HYDROGEN)
# floor0 = microchip(HYDROGEN) | microchip(LITHIUM)

current_floor = 0
initial_state = hash_state(current_floor, floor0, floor1, floor2, floor3)

all = generator(POLONIUM) | microchip(POLONIUM) | \
      generator(THULIUM) | microchip(THULIUM) | \
      generator(PROMETHIUM) | microchip(PROMETHIUM) | \
      generator(RUTHENIUM) | microchip(RUTHENIUM) | \
      generator(COBALT) | microchip(COBALT)
# all = generator(LITHIUM) | microchip(LITHIUM) | \
#       generator(HYDROGEN) | microchip(HYDROGEN) 
floor3_complete = all << (2 + (2 * NUMBER_OF_TYPES * 3))

def floor_is_valid(state:int, floor_number: int):
  # If the floor contains at least one generator,  then all microchips must have their matching generators
  
  offset = bit_offset(floor_number)
  has_generator = False
  for i in range(NUMBER_OF_TYPES):
    if test_bit(state, offset + i + NUMBER_OF_TYPES):
      has_generator = True
  if not has_generator:
    return True

  for i in range(NUMBER_OF_TYPES):
    if test_bit(state, offset + i) and not test_bit(state, offset + i + NUMBER_OF_TYPES):
      return False  # Microchip without a generator
  return True


all_bits = list(range(0, NUMBER_OF_TYPES * 2))
def generate_moves():
  bits_to_move = []
  for bit in all_bits:
    bits_to_move.append([bit])
  for bits in combinations(all_bits, r=2):
    bits_to_move.append(bits)
  return bits_to_move

def possible_moves(state: int) -> List[int]:
  valid_moves = []
  floor_no = state & 0b11

  for to_move in generate_moves():
    if test_item_bits(state, floor_no, to_move):
      # Would this floor be valid without them?
      removed_from_floor = clear_item_bits(state, floor_no, to_move)
      if floor_is_valid(removed_from_floor, floor_no):
        if floor_no > 0:
          amended_floor = set_item_bits(removed_from_floor, floor_no-1, to_move)
          if floor_is_valid(amended_floor, floor_no-1):
            # Moving down is fine
            valid_moves.append(set_floor_bits(amended_floor, floor_no-1))

        if floor_no < 3:
          amended_floor = set_item_bits(removed_from_floor, floor_no+1, to_move)
          if floor_is_valid(amended_floor, floor_no+1):
            # Moving up is fine
            valid_moves.append(set_floor_bits(amended_floor, floor_no+1))

  return valid_moves

def solve(state, route, seen):
  if len(route) > 100: return len(route)
  # Success!
  if (state & floor3_complete) == floor3_complete:
    return len(route)

  best_route = 99999
  for next_state in possible_moves(state):
    if next_state not in route:
      depth = seen.get(next_state, 9999)
      if len(route) < depth:
        seen[next_state] = len(route)
        best_route = min(best_route, solve(next_state, route + [state], seen))
  return best_route

print(solve(initial_state, [], dict()))
