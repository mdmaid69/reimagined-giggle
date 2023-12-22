import datetime
def get_current_datetime():
        return datetime.datetime.now()
import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)