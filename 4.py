import sys

input_file = sys.argv[1] if len(sys.argv) > 1 else "4.in"
lines = [l.strip() for l in open(input_file).readlines()]
ranges = [[[int(s) for s in l.split("-")] for l in line.split(",")] for line in lines]

p1, p2 = 0, 0
for r in ranges:
	x1, y1, x2, y2 = *r[0], *r[1]
	p1 += 1 if x1 <= x2 and y1 >= y2 or x2 <= x1 and y2 >= y1 else 0
	p2 += 1 if x1 <= x2 and y1 >= x2 or x1 >= x2 and y2 >= x1 else 0

print(p1)
print(p2)
