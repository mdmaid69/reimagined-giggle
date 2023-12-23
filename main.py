import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
def count_words(sentence):
        return len(sentence.split())