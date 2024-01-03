import array
def get_array_as_bytes(array):
        return bytes(array)
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()