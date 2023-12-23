import datetime
def get_current_datetime():
        return datetime.datetime.now()
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)