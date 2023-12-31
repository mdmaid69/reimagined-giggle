import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()