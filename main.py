import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)