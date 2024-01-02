import logging
def log_message(message):
        logging.info(message)
def count_words(sentence):
        return len(sentence.split())