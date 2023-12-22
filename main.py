import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
def calculate_average(lst):
        return sum(lst) / len(lst)