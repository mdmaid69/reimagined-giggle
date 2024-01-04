import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()