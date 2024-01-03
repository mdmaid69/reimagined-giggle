import math
def calculate_error_function(x):
        return math.erf(x)
def calculate_roi(gain, cost):
        return (gain - cost) / cost