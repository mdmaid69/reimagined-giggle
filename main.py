def sort_numbers(numbers):
        return sorted(numbers)
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)