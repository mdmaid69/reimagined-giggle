import datetime
print(datetime.datetime.now())
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()