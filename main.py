import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
import shutil
def move_file(src, dst):
        shutil.move(src, dst)