sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))
import logging
def setup_logging(level):
        logging.basicConfig(level=level)