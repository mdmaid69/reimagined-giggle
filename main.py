import re
print(re.match("h.*o", "hello world"))
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()