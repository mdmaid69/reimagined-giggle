def calculate_average(numbers):
        return sum(numbers) / len(numbers)
def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b