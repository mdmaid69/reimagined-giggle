import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
import logging
def setup_logging(level):
        logging.basicConfig(level=level)