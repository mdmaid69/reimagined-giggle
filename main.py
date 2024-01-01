import platform
def get_python_version():
        return platform.python_version()
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)