def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time
import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)