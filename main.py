def calculate_average(numbers):
        return sum(numbers) / len(numbers)
n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])