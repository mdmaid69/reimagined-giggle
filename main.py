import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
import tensorflow as tf
print(tf.__version__)