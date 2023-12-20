import time
def get_time_since_epoch():
        return time.time()
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)