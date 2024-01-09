import math
def calculate_complementary_error_function(x):
        return math.erfc(x)
def calculate_roi(gain, cost):
        return (gain - cost) / cost