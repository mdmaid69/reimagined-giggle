import logging
def log_message(message):
        logging.info(message)
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b