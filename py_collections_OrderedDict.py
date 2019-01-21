# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
N = int(input())
items_dict = OrderedDict()
for _ in range(N):
    unpacked_items = input().strip().split()
    if len(unpacked_items) == 3:
        item_name = unpacked_items[0] + ' ' + unpacked_items[1]
        net_price = unpacked_items[2]
    else:
        item_name = unpacked_items[0]
        net_price = unpacked_items[1]
    if item_name not in items_dict:
        items_dict[item_name] = str(net_price)
    else:
        items_dict[item_name] = items_dict[item_name] + ' ' + str(net_price)
        
for k,v in items_dict.items():
    print (k, sum(list(map(int,v.split(' ')))))