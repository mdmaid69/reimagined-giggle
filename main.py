import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")