def second_largest(arr):
    largest = -1
    second = -1
    for num in arr:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num
    return second

print(second_largest([12, 35, 1, 10, 34, 1]))
print(second_largest([10, 5, 10]))
print(second_largest([10, 10, 10]))
