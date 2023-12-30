import platform
def get_os_info():
        return platform.uname()
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()