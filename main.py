n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])
def sort_numbers(numbers):
        return sorted(numbers)