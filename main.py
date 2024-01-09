import math
def calculate_sign(x):
        return math.copysign(1, x)
import os
def get_environment_variable(var):
        return os.getenv(var)