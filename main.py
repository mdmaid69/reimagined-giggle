def calculate_perpetuity(payment, rate):
        return payment / rate
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)