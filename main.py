def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time
import math
def calculate_complementary_error_function(x):
        return math.erfc(x)