import array
def convert_array_to_unicode(array):
        return array.tounicode()
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()