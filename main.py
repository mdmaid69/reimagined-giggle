import os
def get_environment_variable(var):
        return os.getenv(var)
def calculate_roi(gain, cost):
        return (gain - cost) / cost