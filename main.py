import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
import array
def append_to_array(array, item):
        array.append(item)