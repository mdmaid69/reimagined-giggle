import logging
def log_message(message):
        logging.info(message)
def find_unique_words(sentence):
        return set(sentence.split())