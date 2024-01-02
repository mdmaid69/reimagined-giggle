import logging
def setup_logging(level):
        logging.basicConfig(level=level)
n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])