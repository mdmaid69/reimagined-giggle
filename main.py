import platform
def get_python_version():
        return platform.python_version()
def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps