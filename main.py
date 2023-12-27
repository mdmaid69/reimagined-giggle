def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)
import logging
def log_message(message):
        logging.info(message)