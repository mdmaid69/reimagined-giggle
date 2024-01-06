import array
def get_array_buffer_info(array):
        return array.buffer_info()
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()