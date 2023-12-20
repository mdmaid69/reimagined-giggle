def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
numbers = [1, 2, 3, 4, 5]
print("Squared:", [n**2 for n in numbers])