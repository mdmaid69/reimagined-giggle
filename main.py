def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)