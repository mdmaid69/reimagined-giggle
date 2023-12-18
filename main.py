import re
def split_string(pattern, string):
        return re.split(pattern, string)
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()