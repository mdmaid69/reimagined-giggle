numbers = [1, 2, 3, 4, 5]
print("Even:", [n for n in numbers if n % 2 == 0])
def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal