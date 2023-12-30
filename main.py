def calculate_interest(principal, rate, time):
        return principal * (1 + rate)**time
import platform
def get_os_info():
        return platform.uname()