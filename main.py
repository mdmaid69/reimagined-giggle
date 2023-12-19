import array
def convert_array_to_bytes(array):
        return array.tobytes()
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()