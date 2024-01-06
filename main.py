import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()