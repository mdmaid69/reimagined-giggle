import logging
def setup_logging(level):
        logging.basicConfig(level=level)
def count_characters(sentence):
        return len(sentence)