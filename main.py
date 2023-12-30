def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)
def calculate_perpetuity(payment, rate):
        return payment / rate