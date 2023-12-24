import logging
def setup_logging(level):
        logging.basicConfig(level=level)
def find_unique_words(sentence):
        return set(sentence.split())