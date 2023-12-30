def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
import logging
def setup_logging(level):
        logging.basicConfig(level=level)