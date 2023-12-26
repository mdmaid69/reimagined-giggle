import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
import array
def convert_array_to_string(array):
        return array.tostring()