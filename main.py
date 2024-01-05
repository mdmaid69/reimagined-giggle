import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
import array
def iterate_over_array(array):
        for item in array:
        print(item)