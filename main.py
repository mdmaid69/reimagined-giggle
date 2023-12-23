def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time