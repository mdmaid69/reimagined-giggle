def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time
import os
def get_environment_variable(var):
        return os.getenv(var)