import array
def get_array_as_float(array):
        return float(array[0])
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()