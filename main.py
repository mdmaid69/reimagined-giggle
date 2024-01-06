import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
import array
def check_if_array_contains_item(array, item):
        return item in array