import tensorflow as tf
print(tf.__version__)
import platform
def get_os_info():
        return platform.uname()