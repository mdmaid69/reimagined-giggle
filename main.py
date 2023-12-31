import logging
def setup_logging(level):
        logging.basicConfig(level=level)
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())