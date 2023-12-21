def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b
numbers = [1, 2, 3, 4, 5]
print("Sum:", sum(numbers))