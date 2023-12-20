import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())