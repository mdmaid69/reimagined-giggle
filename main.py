import sklearn.datasets
print(sklearn.datasets.load_iris())
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()