import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)