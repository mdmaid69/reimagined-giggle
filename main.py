n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])
def calculate_simple_interest(principal, rate, time):
        return principal * rate * time