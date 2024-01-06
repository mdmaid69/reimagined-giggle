import os
def get_environment_variable(var):
        return os.getenv(var)
def calculate_pressure(force, area):
        return force / area