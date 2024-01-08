import platform
def get_os_info():
        return platform.uname()
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)