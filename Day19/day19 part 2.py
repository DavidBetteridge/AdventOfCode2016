from math import floor
from dataclasses import dataclass
from typing import Optional

@dataclass
class Node:
  value: int
  next_node: Optional["Node"]

def forward(node: Node, steps: int) -> Node:
  for _ in range(steps):
    node = node.next_node
  return node

n = 3017957

first_node = Node(1, None)
node = first_node
for value in range(n, 1, -1):
  previous_node = Node(value, node)
  node = previous_node
first_node.next_node = node


current_elf = first_node
elf_before_target = forward(first_node, floor(n/2)-1)
shift=True
while n > 1:
  n -= 1
  elf_before_target.next_node = elf_before_target.next_node.next_node
  if shift:
    elf_before_target = elf_before_target.next_node
  shift = not shift
  current_elf = current_elf.next_node
print(current_elf.value)  