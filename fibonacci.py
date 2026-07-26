def fibonacci_iterative(n):
    a, b = 0, 1
    result = []
    
    for i in range(n):
        result.append(a)
        a, b = b, a + b
    
    return result

print(fibonacci_iterative(7))   # [0, 1, 1, 2, 3, 5, 8]


def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

for i in range(7):
    print(fibonacci_recursive(i), end=" ")
# Output: 0 1 1 2 3 5 8
