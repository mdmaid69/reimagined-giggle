import collections
def create_user_string():
        return collections.UserString()
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()