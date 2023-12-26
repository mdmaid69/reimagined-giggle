import platform
def get_os_info():
        return platform.uname()
def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time