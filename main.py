def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())