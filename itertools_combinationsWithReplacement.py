# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement

s, k = input().strip().split()

for c in combinations_with_replacement(sorted(s), int(k)):
    print("".join(c))


