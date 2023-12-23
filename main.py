import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())