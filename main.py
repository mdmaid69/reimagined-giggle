import itertools
print(list(itertools.permutations([1, 2, 3])))
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()