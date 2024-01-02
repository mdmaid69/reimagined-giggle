import tensorflow as tf
print(tf.__version__)
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)