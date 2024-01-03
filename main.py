import tensorflow as tf
print(tf.__version__)
import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)