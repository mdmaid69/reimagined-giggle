import logging
def log_message(message):
        logging.info(message)
def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)