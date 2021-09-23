from collections import OrderedDict
n = int(input())
d = OrderedDict()
for i in range(n):
    item,space,quantity = input().rpartition('')
    d[item] = d.get(item,0) + int(quantity)

for item,quantity in d.items():
    print(item,quantity)