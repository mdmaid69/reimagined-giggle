import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
import array
def clear_array(array):
        array *= 0