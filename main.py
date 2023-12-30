import random
def roll_die():
        return random.randint(1, 6)
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()