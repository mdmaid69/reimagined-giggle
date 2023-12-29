text = "Hello, world!"
print("Is palindrome:", text == text[::-1])
import logging
def setup_logging(level):
        logging.basicConfig(level=level)