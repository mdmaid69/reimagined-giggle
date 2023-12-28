import logging
def log_message(message):
        logging.info(message)
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))