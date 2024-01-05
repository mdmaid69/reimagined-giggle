import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
import array
def reverse_array(array):
        array.reverse()