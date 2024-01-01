import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()