def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)
def calculate_perimeter_triangle(a, b, c):
        return a + b + c