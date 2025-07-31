def merge_lists_plus(a, b):
    return a + b

def merge_lists(a, b):
    a.extend(b)
    return a

print(merge_lists_plus([1, 2, 7], [3, 4, 8]))
print(merge_lists([1, 2], [3, 4]))