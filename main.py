import random
def generate_random_sample(population, k):
        return random.sample(population, k)
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()