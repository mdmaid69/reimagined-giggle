def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)
numbers = [1, 2, 3, 4, 5]
print("Average:", sum(numbers) / len(numbers))