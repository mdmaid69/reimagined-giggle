import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
def count_words(sentence):
        return len(sentence.split())