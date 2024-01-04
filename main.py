import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()