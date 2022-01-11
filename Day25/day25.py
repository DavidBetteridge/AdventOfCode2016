import dataclasses

with open('C:\Personal\AdventOfCode2016\Day25\data.txt') as f:
  instructions = [line.strip() for line in f.readlines()]


@dataclasses.dataclass
class Machine:
  a = 0
  b = 0
  c = 0
  d = 0
  ip = 0

  def set(self, register, value):
    setattr(self, register, value)

  def get(self, register_or_value: str):
    if register_or_value.isalpha():
      return int(getattr(self, register_or_value))
    else:
      return int(register_or_value)

  def run(self, output_fn):
    while self.ip < len(instructions):
      parts = instructions[self.ip].split(" ")
      command = parts[0]

      if command == "cpy":
        if parts[2].isalpha():
          self.set(parts[2], self.get(parts[1]))
        self.ip += 1

      elif command == "tgl":
        idx_command_to_toggle = self.ip + self.get(parts[1])
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
        self.ip += 1

      elif command == "inc":
        if parts[1].isalpha():
          self.set(parts[1], self.get(parts[1])+1)
        self.ip += 1
      elif command == "dec":
        if parts[1].isalpha():
          self.set(parts[1], self.get(parts[1])-1)
        self.ip += 1
      elif command == "jnz":
        if self.get(parts[1]) == 0:
          self.ip += 1
        else:
          self.ip += self.get(parts[2])

      elif command == "out":
        if not check_output(self.get(parts[1])):
          break
        self.ip += 1


last_output = 1
def check_output(value: int):
  global last_output
  if value == last_output:
    last_output = 1
    return False
  else:
    last_output = value
    return True


a = 1
machine = Machine()
while True:
  print(a)
  machine.a = a
  machine.b = 0
  machine.c = 0
  machine.d = 0
  machine.ip = 0
  machine.run(check_output)
  a+=1


  #196