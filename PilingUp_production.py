T = int(input())
for t in range(T):
    N = int(input())
    lst = list(map(int, input().strip().split()))
    L = len(lst)
    i = 0
    while i < L - 1 and lst[i] >= lst[i+1]:
        i += 1
    while i < L - 1 and lst[i] <= lst[i+1]:
        i += 1
    print ("Yes" if i == L - 1 else "No")