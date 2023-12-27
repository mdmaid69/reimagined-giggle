import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
import tensorflow as tf
print(tf.__version__)