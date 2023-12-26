import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
import array
def get_array_as_format(array, format_spec):
        return format(array, format_spec)