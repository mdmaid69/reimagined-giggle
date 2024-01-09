import logging
def log_message(message):
        logging.info(message)
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())