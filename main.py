import platform
def get_python_version():
        return platform.python_version()
import tensorflow as tf
print(tf.__version__)