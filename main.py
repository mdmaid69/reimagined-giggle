import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
def is_palindrome(s):
        return s == s[::-1]