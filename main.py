import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
def calculate_eps(net_income, shares_outstanding):
        return net_income / shares_outstanding