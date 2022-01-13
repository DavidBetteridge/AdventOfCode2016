from collections import Counter

with open('Day06/data.txt') as f:
  signals = [line.strip() for line in f.readlines()]


result = ""
for column_number in range(len(signals[0])):
  column = []
  for signal in signals:
    column.append(signal[column_number])
  counts = Counter(column)
  result += counts.most_common(1)[0][0]
print(result)