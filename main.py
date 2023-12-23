sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()