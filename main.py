list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Union:", set(list1) | set(list2))
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()