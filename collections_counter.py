# Enter your code here. Read input from STDIN. Print output to STDOUT

X = int(input())
shoe_sizes = list(map(int,input().strip().split()))

N = int(input())

earned_amount = []
for n in range(N):
    desired_size,price = list(map(int,input().strip().split()))
    if desired_size in shoe_sizes:
        earned_amount.append(price)
        shoe_sizes.remove(desired_size)

print (sum(earned_amount))
