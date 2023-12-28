def calculate_interest(principal, rate, time):
        return principal * (1 + rate)**time
n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])