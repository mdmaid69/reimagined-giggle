import collections
def create_user_list():
        return collections.UserList()
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()