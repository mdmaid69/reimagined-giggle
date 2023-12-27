import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)
import time
def wait_for_seconds(seconds):
        time.sleep(seconds)