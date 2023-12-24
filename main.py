import logging
def setup_logging(level):
        logging.basicConfig(level=level)
text = "Hello, world!"
print("Reversed:", text[::-1])