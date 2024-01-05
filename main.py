import platform
def get_python_version():
        return platform.python_version()
def calculate_interest(principal, rate, time):
        return principal * (1 + rate)**time