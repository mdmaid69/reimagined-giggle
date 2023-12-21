import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
def calculate_current_ratio(current_assets, current_liabilities):
        return current_assets / current_liabilities