import logging
def setup_logging(level):
        logging.basicConfig(level=level)
def calculate_volume(length, width, height):
        return length * width * height