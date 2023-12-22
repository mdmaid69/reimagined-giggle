import tensorflow as tf
print(tf.__version__)
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()