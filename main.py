import array
def get_array_as_bytearray(array):
        return bytearray(array)
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()