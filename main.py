import tensorflow as tf
print(tf.__version__)
import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)