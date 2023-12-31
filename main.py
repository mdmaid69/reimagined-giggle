import tensorflow as tf
print(tf.__version__)
import getpass
def get_username():
        return getpass.getuser()