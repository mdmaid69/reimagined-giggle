numbers = [1, 2, 3, 4, 5]
print("Sum:", sum(numbers))
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)