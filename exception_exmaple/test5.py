
data = [
    [1,2,2,3,3,4,5,6,7,8],
    [1,2,3,9,10,11,19],
    [14,15,16,18,20,21],
    [1,2,3],
    [22,21,23,24],
    [30,31,32],
    [33,35,36],
]

import itertools

for items in itertools.combinations(data,4):
    total_list_item = []
    total_item_length = 0
    for item in items:
        total_item_length += len(set(item))
        total_list_item +=item
    if total_item_length != len(set(total_list_item)):
        continue
    print(items)

