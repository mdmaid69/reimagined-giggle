import tensorflow as tf
print(tf.__version__)
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)