import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
def remove_duplicates(lst):
        return list(set(lst))