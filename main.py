import time
def get_current_time():
        return time.ctime()
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()