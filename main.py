def calculate_average(numbers):
        return sum(numbers) / len(numbers)
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)