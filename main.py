numbers = [1, 2, 3, 4, 5]
print("Sum:", sum(numbers))
def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)