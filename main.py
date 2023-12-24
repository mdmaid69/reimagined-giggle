def calculate_area(radius):
        return 3.14 * radius * radius
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)