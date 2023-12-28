def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal
import platform
def get_os_info():
        return platform.uname()