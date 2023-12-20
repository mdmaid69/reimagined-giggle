import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
import time
def get_time_since_epoch():
        return time.time()