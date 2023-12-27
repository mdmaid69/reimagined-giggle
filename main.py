import time
def get_time_since_epoch():
        return time.time()
def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps