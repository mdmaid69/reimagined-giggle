import array
def get_array_item_count(array, item):
        return array.count(item)
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()