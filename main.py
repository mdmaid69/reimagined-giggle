text = "Hello, world!"
print("Is palindrome:", text == text[::-1])
import logging
def log_message(message):
        logging.info(message)