import os
def get_environment_variable(var):
        return os.getenv(var)
import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)