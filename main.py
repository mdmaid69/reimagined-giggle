def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)
def calculate_interest(principal, rate, time):
        return principal * (1 + rate)**time