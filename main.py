import sys
def exit_program():
        sys.exit()
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()