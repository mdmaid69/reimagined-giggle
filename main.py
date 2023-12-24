import array
def get_array_length(array):
        return len(array)
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()