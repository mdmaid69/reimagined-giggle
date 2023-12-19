def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)
def calculate_simple_interest(principal, rate, time):
        return principal * rate * time