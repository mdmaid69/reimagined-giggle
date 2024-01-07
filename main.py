def count_characters(sentence):
        return len(sentence)
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()