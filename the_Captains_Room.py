k = int(input())

arr = list(map(int, input().split()))

my_set = set(arr)

print(((sum(my_set)*k)-(sum(arr)))//(k-1))