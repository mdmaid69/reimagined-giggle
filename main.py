import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)