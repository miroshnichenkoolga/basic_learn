def double_dict_values(d):
    return dict(map(lambda item: (item[0], item[1] *2), d.items()))

print(double_dict_values({'a': 1, 'b': 2, 'c': 3}))