def calculate_average(numbers):
        return sum(numbers) / len(numbers)
def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)