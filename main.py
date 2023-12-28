import logging
def setup_logging(level):
        logging.basicConfig(level=level)
i = 0
while i < 5:
        print(i)
        i += 1