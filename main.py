import logging
def log_message(message):
        logging.info(message)
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)