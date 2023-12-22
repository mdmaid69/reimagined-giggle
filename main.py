import logging
def log_message(message):
        logging.info(message)
n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])