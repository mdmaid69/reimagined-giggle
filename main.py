n = 10
print("Prime numbers:", [x for x in range(2, n) if all(x % i != 0 for i in range(2, int(x**0.5) + 1))])
def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal