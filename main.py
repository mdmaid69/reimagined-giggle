def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal
import time
def get_time_since_epoch():
        return time.time()