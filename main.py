import random
def generate_random_number(start, end):
        return random.randint(start, end)
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()