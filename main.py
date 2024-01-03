n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)