def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())