import logging
def setup_logging(level):
        logging.basicConfig(level=level)
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))