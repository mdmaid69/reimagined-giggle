i = 0
while i < 5:
        print(i)
        i += 1
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)