import tensorflow as tf
print(tf.__version__)
import getpass
def get_password(prompt):
        return getpass.getpass(prompt)