import time
def get_current_time():
        return time.ctime()
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)