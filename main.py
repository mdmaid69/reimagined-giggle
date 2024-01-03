def calculate_interest(principal, rate, time):
        return principal * (1 + rate)**time
import time
def get_current_time():
        return time.ctime()