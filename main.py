import matplotlib.pyplot as plt
plt.plot([1, 2, 3], [4, 5, 6])
plt.show()
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()