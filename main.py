import logging
def log_message(message):
        logging.info(message)
n = 10
print("Powers of 2:", [2**x for x in range(n)])