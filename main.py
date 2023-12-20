def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)
import time
def wait_for_seconds(seconds):
        time.sleep(seconds)