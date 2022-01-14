import dataclasses
import re
from typing import Dict, List, Optional

@dataclasses.dataclass
class Bot:
  values: List[int] = dataclasses.field(default_factory=list)
  low_bot : Optional[int] = dataclasses.field(default=None)
  low_output : Optional[int] = dataclasses.field(default=None)
  high_bot : Optional[int] = dataclasses.field(default=None)
  high_output : Optional[int] = dataclasses.field(default=None)

with open('Day10/data.txt') as f:
  instructions = [line.strip() for line in f.readlines()]

bots: Dict[int, Bot] = {}
output: Dict[int, int] = {}

for instruction in instructions:
  if instruction.startswith("value"):
    matches = re.match("value ([0-9]+) goes to bot ([0-9]+)",instruction)
    value = int(matches.groups(0)[0])
    bot_number = int(matches.groups(0)[1])
    if bot_number not in bots:
      bots[bot_number] = Bot()
    bots[bot_number].values.append(value)      
  else:
    matches = re.match(r"bot ([0-9]+) gives low to (output [0-9]+|bot [0-9]+) and high to (output [0-9]+|bot [0-9]+)",instruction)
    source_bot_number = int(matches.groups(0)[0])
    low_instruction = matches.groups(0)[1]
    high_instruction = matches.groups(0)[2]

    if source_bot_number not in bots:
      bots[source_bot_number] = Bot()

    if "bot" in low_instruction:
      bots[source_bot_number].low_bot = int(low_instruction[4:])
    else:
      bots[source_bot_number].low_output = int(low_instruction[7:])

    if "bot" in high_instruction:
      bots[source_bot_number].high_bot = int(high_instruction[4:])
    else:
      bots[source_bot_number].high_output = int(high_instruction[7:])

no_progress = False
while not no_progress:
  no_progress = True
  for bot_number, bot in bots.items():
    if len(bot.values) == 2:
      if 17 in bot.values and 61 in bot.values:
        print(bot_number)  #147

      lower = min(bot.values)
      if bot.low_bot is not None:
        bots[bot.low_bot].values.append(lower)
      elif bot.low_output is not None:
        output[bot.low_output] = lower
      
      higher = max(bot.values)
      if bot.high_bot is not None:
        bots[bot.high_bot].values.append(higher)
      elif bot.high_output is not None:
        output[bot.high_output] = higher

      bot.values = []
      no_progress = False

print(output[0] * output[1] * output[2])  #55637