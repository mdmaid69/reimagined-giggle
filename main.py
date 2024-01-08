import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()