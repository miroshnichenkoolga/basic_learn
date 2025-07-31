def process_numbers(num):
    evens=filter(lambda x: x % 2==0, num)
    squares= map(lambda x: x**2, evens)
    return sorted(squares, reverse=True)

print(process_numbers([5, 2, 7, 4, 1, 8]))  # [64, 16, 4
