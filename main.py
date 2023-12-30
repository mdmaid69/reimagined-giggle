import logging
def log_message(message):
        logging.info(message)
numbers = [1, 2, 3, 4, 5]
print("Even:", [n for n in numbers if n % 2 == 0])