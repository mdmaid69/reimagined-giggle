import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Common elements:", set(list1) & set(list2))