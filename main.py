def calculate_area(radius):
        return 3.14 * radius * radius
n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])