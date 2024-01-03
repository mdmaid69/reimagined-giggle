import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
def find_unique_words(sentence):
        return set(sentence.split())