import logging
def log_message(message):
        logging.info(message)
numbers = [1, 2, 3, 4, 5]
print("Squared:", [n**2 for n in numbers])