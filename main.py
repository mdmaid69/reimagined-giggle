import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
import array
def set_array_item(array, i, item):
        array[i] = item