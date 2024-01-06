def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)
def calculate_average(numbers):
        return sum(numbers) / len(numbers)