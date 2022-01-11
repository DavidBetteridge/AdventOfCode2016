import dataclasses

with open('C:\Personal\AdventOfCode2016\Day12\data.txt') as f:
  instructions = [line.strip() for line in f.readlines()]


@dataclasses.dataclass
class Machine:
  a = 0
  b = 0
  c = 0
  d = 0
  ip = 0

machine = Machine()
machine.c = 1  #Part 2

def set(register, value):
  setattr(machine, register, value)

def get(register_or_value: str):
  if register_or_value.isalpha():
    return int(getattr(machine, register_or_value))
  else:
    return int(register_or_value)

while machine.ip < len(instructions):
  parts = instructions[machine.ip].split(" ")
  command = parts[0]

  if command == "cpy":
    set(parts[2], get(parts[1]))
    machine.ip += 1
  elif command == "inc":
    set(parts[1], get(parts[1])+1)
    machine.ip += 1
  elif command == "dec":
    set(parts[1], get(parts[1])-1)    
    machine.ip += 1
  elif command == "jnz":
    if get(parts[1]) == 0:
      machine.ip += 1
    else:
      machine.ip += get(parts[2])

print(machine.a, machine.b, machine.c, machine.d)      
