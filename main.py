def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
numbers = [1, 2, 3, 4, 5]
print("Sum:", sum(numbers))