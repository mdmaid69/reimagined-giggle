sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))
import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")