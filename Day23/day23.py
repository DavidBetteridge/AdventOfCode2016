import dataclasses

with open('C:\Personal\AdventOfCode2016\Day23\data.txt') as f:
  instructions = [line.strip() for line in f.readlines()]


@dataclasses.dataclass
class Machine:
  a = 0
  b = 0
  c = 0
  d = 0
  ip = 0

machine = Machine()
machine.a = 7

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
    if parts[2].isalpha():
      set(parts[2], get(parts[1]))
    machine.ip += 1

  elif command == "tgl":
    idx_command_to_toggle = machine.ip + get(parts[1])
    if 0 <= idx_command_to_toggle < len(instructions):
      current = instructions[idx_command_to_toggle]
      args = current.split(" ")
      arity = len(args) - 1

      if arity == 1:
        if args[0] == "inc":
          current = f"dec {args[1]}"
        else:
          current = f"inc {args[1]}"
      elif arity == 2:
        if args[0] == "jnz":
          current = f"cpy {args[1]} {args[2]}"
        else:
          current = f"jnz {args[1]} {args[2]}"

      instructions[idx_command_to_toggle] = current
    machine.ip += 1

  elif command == "inc":
    if parts[1].isalpha():
      set(parts[1], get(parts[1])+1)
    machine.ip += 1
  elif command == "dec":
    if parts[1].isalpha():
      set(parts[1], get(parts[1])-1)
    machine.ip += 1
  elif command == "jnz":
    if get(parts[1]) == 0:
      machine.ip += 1
    else:
      machine.ip += get(parts[2])

  # print(machine.a, machine.b, machine.c, machine.d)
print(machine.a)



#210 too low