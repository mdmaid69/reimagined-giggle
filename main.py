import time
def get_time_since_epoch():
        return time.time()
def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time