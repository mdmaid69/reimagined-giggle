import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))