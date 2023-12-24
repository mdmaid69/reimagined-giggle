import logging
def log_message(message):
        logging.info(message)
n = 10
print("Cube numbers:", [x**3 for x in range(n)])