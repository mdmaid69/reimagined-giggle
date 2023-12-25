import getpass
def get_username():
        return getpass.getuser()
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()