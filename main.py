def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)
import platform
def get_python_version():
        return platform.python_version()