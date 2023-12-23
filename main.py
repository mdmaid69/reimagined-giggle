def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)
import time
def wait_for_seconds(seconds):
        time.sleep(seconds)