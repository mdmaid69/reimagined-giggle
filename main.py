def count_words(sentence):
        return len(sentence.split())
import logging
def setup_logging(level):
        logging.basicConfig(level=level)