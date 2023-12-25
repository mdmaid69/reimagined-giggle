import time
def wait_for_seconds(seconds):
        time.sleep(seconds)
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()