import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
def calculate_return_on_assets(net_income, total_assets):
        return net_income / total_assets