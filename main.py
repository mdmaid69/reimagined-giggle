import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
import random
def roll_die():
        return random.randint(1, 6)