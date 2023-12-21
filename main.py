n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)