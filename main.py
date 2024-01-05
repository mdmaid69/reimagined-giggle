import array
def pop_from_array(array, i=-1):
        return array.pop(i)
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()