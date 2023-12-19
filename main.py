import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()