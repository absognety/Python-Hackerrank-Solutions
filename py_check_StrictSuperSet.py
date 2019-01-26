# Enter your code here. Read input from STDIN. Print output to STDOUT

nA_elements = set(map(int,input().strip().split()))
num_others = int(input())
inds = []
for s in range(num_others):
    other_set = set(map(int,input().strip().split()))
    if (nA_elements.issuperset(other_set)) and (nA_elements != other_set):
        inds.append(True)
    else:
        inds.append(False)

if (len(set(inds))==1) and (inds[0]==True):
    print (True)
else:
    print (False)