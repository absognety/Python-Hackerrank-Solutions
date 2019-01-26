# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
elements_A = set(map(int,input().strip().split()))
num_others = int(input())
for I in range(num_others):
    operation,_ = input().strip().split()
    entries_other = set(map(int,input().strip().split()))
    if operation == 'update':
        elements_A.update(entries_other)
    elif operation == 'intersection_update':
        elements_A.intersection_update(entries_other)
    elif operation == 'difference_update':
        elements_A.difference_update(entries_other)
    elif operation == 'symmetric_difference_update':
        elements_A.symmetric_difference_update(entries_other)

print (sum(elements_A))
