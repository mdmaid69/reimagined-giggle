import numpy as np
print(np.array([1, 2, 3]))
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()