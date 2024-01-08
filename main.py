import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
import math
def calculate_complementary_error_function(x):
        return math.erfc(x)