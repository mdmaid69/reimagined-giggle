def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)
numbers = [1, 2, 3, 4, 5]
print("Squared:", [n**2 for n in numbers])