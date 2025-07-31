def pop_until_zero(nums):
    result =[]
    while nums:
        value = nums.pop()
        if value == 0:
            break
        result.append(value)
    return result

print(pop_until_zero([5, 3, 1, 0, 7, 8]))
