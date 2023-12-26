import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)
def calculate_roi(gain, cost):
        return (gain - cost) / cost