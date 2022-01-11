from collections import Counter

with open('Day06/data.txt') as f:
  signals = [line.strip() for line in f.readlines()]


part1 = ""
part2 = ""
for column_number in range(len(signals[0])):
  column = []
  for signal in signals:
    column.append(signal[column_number])
  counts = Counter(column)
  part1 += counts.most_common(1)[0][0]
  part2 += counts.most_common()[-1][0]
print(part1)
print(part2)