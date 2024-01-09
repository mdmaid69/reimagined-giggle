import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)
import os
def get_environment_variable(var):
        return os.getenv(var)