import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
import getpass
def get_password(prompt):
        return getpass.getpass(prompt)