text_input = '''7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9'''

reports = [[int(v) for v in line.split()] for line in text_input.splitlines()]

def is_safe(report_values):
    diffs = [b - a for a, b in zip(report_values[:-1], report_values[1:])]
    return (all(d > 0 for d in diffs) or all(d < 0 for d in diffs)) and all(1 <= abs(d) <= 3 for d in diffs)

print('Part 1:', sum(
    1 for report in reports if is_safe(report)
))

print('Part 2:', sum(
    1 for report in reports if any(is_safe(report[:i] + report[i + 1:]) for i in range(len(report)))
))
