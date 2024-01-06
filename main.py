def calculate_interest(principal, rate, time):
        return principal * (1 + rate)**time
def calculate_perpetuity(payment, rate):
        return payment / rate