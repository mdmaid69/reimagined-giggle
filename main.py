import array
def remove_from_array(array, item):
        array.remove(item)
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()