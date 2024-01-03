import logging
def log_message(message):
        logging.info(message)
import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)