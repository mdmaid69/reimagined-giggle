import datetime
def get_current_datetime():
        return datetime.datetime.now()
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()