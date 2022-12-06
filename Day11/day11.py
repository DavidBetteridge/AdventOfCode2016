
from itertools import combinations
from typing import Iterable, List


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
  temp = state & ~11
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

# Initial state
floor3 = 0
floor2 = 0
floor1 = microchip(POLONIUM) | microchip(PROMETHIUM)
floor0 = generator(POLONIUM) | generator(THULIUM) | microchip(THULIUM) | \
         generator(PROMETHIUM) | generator(RUTHENIUM) | microchip(RUTHENIUM) | \
         generator(COBALT) | microchip(COBALT)
current_floor = 0
initial_state = hash_state(current_floor, floor0, floor1, floor2, floor3)

all = generator(POLONIUM) | microchip(POLONIUM) | \
      generator(THULIUM) | microchip(THULIUM) | \
      generator(PROMETHIUM) | microchip(PROMETHIUM) | \
      generator(RUTHENIUM) | microchip(RUTHENIUM) | \
      generator(COBALT) | microchip(COBALT)
floor3_complete = all << (2 + (2 * NUMBER_OF_TYPES * 3))

def floor_is_valid(floor_contents:int):
  # If the floor contains at least one generator,  then all microchips must have their matching generators
  if (floor_contents >> NUMBER_OF_TYPES) == 0:
    return True  # No generators
  
  for i in range(NUMBER_OF_TYPES):
    if test_bit(floor_contents, i) and not test_bit(floor_contents, i + NUMBER_OF_TYPES):
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
      if floor_is_valid(removed_from_floor):
        if floor_no > 1:
          amended_floor = set_item_bits(removed_from_floor, floor_no-1, to_move)
          if floor_is_valid(amended_floor):
            # Moving down is fine
            valid_moves.append(set_floor_bits(amended_floor, floor_no-1))

        if floor_no < 3:
          amended_floor = set_item_bits(removed_from_floor, floor_no+1, to_move)
          if floor_is_valid(amended_floor):
            # Moving up is fine
            valid_moves.append(set_floor_bits(amended_floor, floor_no+1))

  return valid_moves


best_depth = 99999
to_process = {initial_state:0}
processed = set()
while len(to_process) > 0:
  next_state, depth = to_process.popitem()
  if next_state not in processed:
    processed.add(next_state)
    for move in possible_moves(next_state):
      if (move & floor3_complete) == floor3_complete:
        best_depth = min(best_depth, depth+1)
      elif move not in processed and move not in to_process:
        to_process[move] = depth+1
print(best_depth)



