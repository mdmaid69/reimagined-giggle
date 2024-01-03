import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)
import os
def get_environment_variable(var):
        return os.getenv(var)