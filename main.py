import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)