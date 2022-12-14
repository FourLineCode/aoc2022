import sys

input_file = sys.argv[1] if len(sys.argv) > 1 else "2.in"
rounds = ["".join(l.strip().split()) for l in open(input_file).readlines()]
results_p1 = {"AX": 4, "AY": 8, "AZ": 3, "BX": 1, "BY": 5, "BZ": 9, "CX": 7, "CY": 2, "CZ": 6}
results_p2 = {"AX": 3, "AY": 4, "AZ": 8, "BX": 1, "BY": 5, "BZ": 9, "CX": 2, "CY": 6, "CZ": 7}
print(sum([results_p1[r] for r in rounds]))
print(sum([results_p2[r] for r in rounds]))
