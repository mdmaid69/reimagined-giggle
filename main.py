import datetime
def get_current_datetime():
        return datetime.datetime.now()
def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps