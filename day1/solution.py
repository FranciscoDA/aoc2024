from collections import Counter
text_input = '''3   4
4   3
2   5
1   3
3   9
3   3'''

lines = [[int(v) for v in line.split()] for line in text_input.splitlines()]
first, second = zip(*lines)
print('Part 1:', sum(
    abs(a - b)
    for a, b in zip(sorted(first), sorted(second))
))

count = Counter(second)
print('Part 2:', sum(
    v * count[v] for v in first
))
