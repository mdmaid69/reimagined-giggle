import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
import array
def get_array_item(array, i):
        return array[i]