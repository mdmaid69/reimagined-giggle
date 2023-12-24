import tensorflow as tf
print(tf.__version__)
import logging
def setup_logging(level):
        logging.basicConfig(level=level)