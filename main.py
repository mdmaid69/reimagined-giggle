import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()