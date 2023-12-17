import sys
def add_to_python_path(path):
        sys.path.append(path)
import tensorflow as tf
print(tf.__version__)