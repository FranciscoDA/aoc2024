import re

regex = re.compile(r"(mul)\((\d+),(\d+)\)|(do)\(\)|(don't)\(\)")

input_text='''xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))'''

result1 = 0
result2 = 0

enabled = True
for mobj in regex.finditer(input_text):
    if mobj.group(1) == 'mul':
        v = int(mobj.group(2)) * int(mobj.group(3))
        result1 += v
        if enabled:
            result2 += v
    elif mobj.group(4) == 'do':
        enabled = True
    elif mobj.group(5) == 'don\'t':
        enabled = False

print('Part 1:', result1)
print('Part 2:', result2)
