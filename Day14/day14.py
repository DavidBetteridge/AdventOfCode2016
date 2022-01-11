
from hashlib import md5
from typing import Optional
from more_itertools import sliding_window
from functools import lru_cache

def find_triple(hash) -> Optional[str]:
  for triple in sliding_window(hash, 3):
    if triple[0] == triple[1] and triple[1] == triple[2]:
      return triple[0]
  return None

@lru_cache(maxsize=None)
def generate_hash(salt: str, index: int) -> str:
  return md5(f"{salt}{index}".encode()).hexdigest()

salt = "cuanljph"
i = 0
keys_found = 0
while keys_found < 64:
  hash = generate_hash(salt, i)
  triple = find_triple(hash)
  if triple is not None:
    to_find = triple * 5
    for j in range(i+1, i+1001):
      hash = generate_hash(salt, j)
      if to_find in hash:
        print("Found key", i, triple)
        keys_found+=1
        break
  i+=1



