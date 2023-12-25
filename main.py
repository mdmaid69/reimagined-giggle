sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))
import logging
def setup_logging(level):
        logging.basicConfig(level=level)