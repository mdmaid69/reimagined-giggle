def reverse_string(s):
        return s[::-1]
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)