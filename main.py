import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
def find_difference(list1, list2):
        return set(list1) - set(list2)