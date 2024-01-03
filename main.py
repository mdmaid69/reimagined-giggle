import os
def get_environment_variable(var):
        return os.getenv(var)
def calculate_perpetuity(payment, rate):
        return payment / rate