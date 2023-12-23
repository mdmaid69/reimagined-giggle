import logging
def setup_logging(level):
        logging.basicConfig(level=level)
def greet(name):
        print(f"Hello, {name}!")