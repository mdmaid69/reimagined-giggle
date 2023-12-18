n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))
def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal