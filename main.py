import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)