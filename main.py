import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
def calculate_debt_ratio(total_debt, total_assets):
        return total_debt / total_assets