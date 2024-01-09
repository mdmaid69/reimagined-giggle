import array
def get_array_as_str(array):
        return str(array)
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()