import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
import array
def get_bytes_from_array(array):
        return array.tobytes()