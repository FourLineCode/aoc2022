import sys

input_file = sys.argv[1] if len(sys.argv) > 1 else "1.in"
lines = open(input_file).read()
calories = sorted([sum([int(n) for n in elf.split("\n")]) for elf in lines.split("\n\n")])
print(calories[-1])
print(sum(calories[-3:]))
