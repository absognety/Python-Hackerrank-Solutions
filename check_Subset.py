# Enter your code here. Read input from STDIN. Print output to STDOUT

T = int(input())
for tcase in range(T):
    nA = int(input())
    nA_elements = set(map(int,input().strip().split()))
    nB = int(input())
    nB_elements = set(map(int,input().strip().split()))
    if nA_elements.issubset(nB_elements):
        print (True)
    else:
        print (False)
