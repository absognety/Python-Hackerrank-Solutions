
from collections import deque
N = int(input())
dequed = deque()
for ops in range(N):
    objs = input().strip().split()
    if len(objs) == 2:
        operation_name,data = objs[0],objs[1]
    else:
        operation_name = objs[0]
    if operation_name=='append':
        dequed.append(data)
    elif operation_name == 'pop':
        dequed.pop()
    elif operation_name == 'popleft':
        dequed.popleft()
    elif operation_name == 'appendleft':
        dequed.appendleft(data)
        
print (' '.join(str(i) for i in dequed))