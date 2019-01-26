# Enter your code here. Read input from STDIN. Print output to STDOUT
nE = int(input())
nE_list = list(map(int,input().strip().split()))

nF = int(input())
nF_list = list(map(int,input().strip().split()))

result = len(set(nE_list)^set(nF_list))
print (result)

