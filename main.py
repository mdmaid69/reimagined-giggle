import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()