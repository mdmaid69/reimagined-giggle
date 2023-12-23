def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")