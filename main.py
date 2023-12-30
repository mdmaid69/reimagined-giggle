n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])
def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal