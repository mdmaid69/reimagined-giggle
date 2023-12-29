import platform
def get_os_info():
        return platform.uname()
def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps