import time
def wait_for_seconds(seconds):
        time.sleep(seconds)
def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time