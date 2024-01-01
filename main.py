import tensorflow as tf
print(tf.__version__)
import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)