def calculate_volume(length, width, height):
        return length * width * height
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()