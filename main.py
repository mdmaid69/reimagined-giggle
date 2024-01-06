n = 10
print("Powers of 2:", [2**x for x in range(n)])
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)