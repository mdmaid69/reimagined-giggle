import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
import array
def get_array_as_int(array):
        return int(array[0])