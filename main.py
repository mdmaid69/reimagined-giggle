text = "Hello, world!"
print("Words:", len(text.split()))
import logging
def setup_logging(level):
        logging.basicConfig(level=level)