import math
def calculate_sign(x):
        return math.copysign(1, x)
def calculate_roi(gain, cost):
        return (gain - cost) / cost