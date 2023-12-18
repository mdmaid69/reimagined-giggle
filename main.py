import tensorflow as tf
print(tf.__version__)
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()