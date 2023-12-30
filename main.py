def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time
import platform
def get_python_version():
        return platform.python_version()