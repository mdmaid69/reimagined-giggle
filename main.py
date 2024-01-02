import array
def insert_into_array(array, i, item):
        array.insert(i, item)
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()