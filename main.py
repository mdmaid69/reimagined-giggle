def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time
def calculate_perpetuity(payment, rate):
        return payment / rate