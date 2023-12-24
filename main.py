import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()