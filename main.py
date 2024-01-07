import logging
def log_message(message):
        logging.info(message)
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)