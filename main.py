import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
import glob
def find_files(pattern):
        return glob.glob(pattern)