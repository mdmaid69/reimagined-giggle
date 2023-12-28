def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
import logging
def log_message(message):
        logging.info(message)