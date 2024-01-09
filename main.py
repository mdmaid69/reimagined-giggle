import tensorflow as tf
print(tf.__version__)
import os
def get_environment_variable(var):
        return os.getenv(var)