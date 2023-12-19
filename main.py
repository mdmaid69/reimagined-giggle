import array
def get_string_from_array(array):
        return array.tobytes()
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()