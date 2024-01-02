import array
def convert_array_to_list(array):
        return array.tolist()
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()