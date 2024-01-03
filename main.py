def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal
import time
def wait_for_seconds(seconds):
        time.sleep(seconds)