import platform
def get_os_info():
        return platform.uname()
def calculate_profit_margin(revenue, cost):
        return (revenue - cost) / revenue