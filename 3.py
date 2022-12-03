import sys

input_file = sys.argv[1] if len(sys.argv) > 1 else "3.in"
lines = [l.strip() for l in open(input_file).readlines()]
groups = [lines[i:i+3] for i in range(0, len(lines), 3)]
get_prio = lambda c: ord(c) - 96 if c > "Z" else ord(c) - 64 + 26

count1, count2 = 0, 0
for line in lines:
	set1, set2 = set(line[:len(line)//2]), set(line[len(line)//2:])
	count1 += get_prio(list(set1.intersection(set2)).pop())

for group in groups:
	set1, set2, set3 = [set(line) for line in group]
	count2 += get_prio(list(set1.intersection(set2).intersection(set3)).pop())

print(count1)
print(count2)